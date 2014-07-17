import unittest
import __builtin__ as builtins

_baseimport = builtins.__import__
_dependencies = dict()
_parent = None


"""
This file contains some prototype function of module reload & denpendencies handle.
Modulised solution can be found at https://github.com/jparise/python-reloader
"""


def _import(name, globals=None, locals=None, fromlist=None, level=-1):
    """
    Created   : 2014.7.15
    Modified  : 2014.7.16

    This script is used to Record Module Dependencies,
    accomplished by installing a custom import hook that
    is called as part of the regular module import machinery..

    Origin from:
    http://www.indelible.org/ink/python-reloading/


    """
    # Track our current parent module.  This is used to find our current
    # place in the dependency graph.

    global _parent
    parent = _parent
    _parent = name

    # Perform the actual import using the base import function.
    m = _baseimport(name, globals, locals, fromlist, level)

    # If we have a parent (i.e. this is a nested import) and this is a
    # reloadable (source-based) module, we append ourself to our parent's
    # dependency list.
    if parent is not None and hasattr(m, '__file__'):
        l = _dependencies.setdefault(parent, [])
        l.append(m)

    # Lastly, we always restore our global _parent pointer.
    _parent = parent

    return m

builtins.__import__ = _import


class Test_import(unittest.TestCase):
    """
    :Time_Created: 2014.7.16

    Unit test for _import.
    """

    def test_one(self):
        import md5
        self.assertGreater(len(_dependencies.keys()), 0)
        # print len(_dependencies.keys())

import imp


def _reload(m, visited):
    """
    Created   : 2014.7.15
    Modified  : 2014.7.16

    Internal module reloading routine.
    """

    name = m.__name__

    # Start by adding this module to our set of visited modules.  We use
    # this set to avoid running into infinite recursion while walking the
    # module dependency graph.
    visited.add(m)

    # Start by reloading all of our dependencies in reverse order.  Note
    # that we recursively call ourself to perform the nested reloads.
    deps = _dependencies.get(name, None)
    if deps is not None:
        for dep in reversed(deps):
            if dep not in visited:
                _reload(dep, visited)

    # Clear this module's list of dependencies.  Some import statements
    # may have been removed.  We'll rebuild the dependency list as part
    # of the reload operation below.
    try:
        del _dependencies[name]
    except KeyError:
        pass

    # Because we're triggering a reload and not an import, the module
    # itself won't run through our _import hook.  In order for this
    # module's dependencies (which will pass through the _import hook) to
    # be associated with this module, we need to set our parent pointer
    # beforehand.
    global _parent
    _parent = name

    # Perform the reload operation.
    imp.reload(m)

    # Reset our parent pointer.
    _parent = None


class Test_reload(unittest.TestCase):
    """
    :Time_Created: 2014.7.16

    Unit test for _reload.
    """

    def test_one(self):
        import md5
        self.assertGreater(len(_dependencies.keys()), 0)
        _reload(md5, set())
        # print len(_dependencies.keys())

if __name__ == "__main__":
    unittest.main()
