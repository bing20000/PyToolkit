"""

Created   : 2014.7.15
Modified  : 2014.7.15

This script is used to Record Module Dependencies,
accomplished by installing a custom import hook that
is called as part of the regular module import machinery..

Origin from:
http://www.indelible.org/ink/python-reloading/


"""

import __builtin__ as builtins

_baseimport = builtins.__import__
_dependencies = dict()
_parent = None


def _import(name, globals=None, locals=None, fromlist=None, level=-1):
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

if __name__ == "__main__":
    import requests
    print _dependencies
