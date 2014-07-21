import string
import random
import unittest


def randomstring(size=6,
                 chars=string.ascii_uppercase + string.ascii_lowercase
                 + string.digits):

    """
    :Time_Created: 2014.7.15

    Constructs random string with given size & charset

    :param size: (optional) desired length of string.
    :param chars: (optional) charset from which string is chosen.

    Usage::

      >>> from string import randomstring
      >>> print randomstring(20)
      aXyGpX1bXx9IqTwF9JjT
    """

    return ''.join(random.choice(chars) for _ in range(size))


class TestRandomString(unittest.TestCase):

    """
    :Time_Created: 2014.7.16

    Unit test for randomstring.
    """

    def test_one(self):
        size = 10
        length = 20
        for i in range(size):
            astr = randomstring(length)
            self.assertEqual(20, len(astr))

from urlparse import urljoin
from urlparse import urlparse
from urlparse import urlunparse
from posixpath import normpath


def urlnormjoin(base, path):
    """
    :Time_Created: 2014.7.16

    A util funciton for url join, add base url & path, also normalize the url.

    This function will
    1> extract the domain(scheme+host) from the 1st param,
    2> join it with the 2nd param
    3> normalize the url  before return.

    :param base: from where the domain is extracted.
    :param path: the postfix to join domain

    Usage::

      >>> from string import randomstring
      >>> urlnormjoin("http://www.baidu.com/123", "/../../abc.html"
      "http://www.baidu.com/abc.html"
    """
    arr0 = urlparse(base)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=arr0)
    url1 = urljoin(domain, path)
    arr = urlparse(url1)
    path = normpath(arr[2])
    return urlunparse((arr.scheme,
                       arr.netloc, path, arr.params, arr.query, arr.fragment))


class TestUrlnormJoin(unittest.TestCase):

    """
    :Time_Created: 2014.7.16

    Unit test for urlnormjoin.
    """

    def test_jion(self):
        self.assertEqual("http://www.baidu.com/abc.html",
                         urlnormjoin("http://www.baidu.com", "abc.html"))
        self.assertEqual("http://www.baidu.com/abc.html",
                         urlnormjoin("http://www.baidu.com",
                                     "/../../abc.html"))
        self.assertEqual("http://www.baidu.com/abc.html",
                         urlnormjoin("http://www.baidu.com/xxx",
                                     "./../../abc.html"))
        self.assertEqual("http://www.baidu.com/abc.html?key=value&m=x",
                         urlnormjoin("http://www.baidu.com",
                                     "abc.html?key=value&m=x"))
        self.assertEqual("http://www.baidu.com/abc.html",
                         urlnormjoin("http://www.baidu.com/123",
                                     "/../../abc.html"))


if __name__ == "__main__":
    unittest.main()
