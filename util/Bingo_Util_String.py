import string
import random
import unittest

"""
Random string generator
:Time_Created: 2014.7.15

A util function to generate random string for given length & charset.
"""


def randomstring(size=6,
                 chars=string.ascii_uppercase + string.ascii_lowercase
                 + string.digits):

    """Constructs random string with given size & charset
    Returns :class:`String<String>` object.

    :param size: (optional) desired length of string.
    :param chars: (optional) charset from which string is chosen.

    Usage::

      >>> from Bingo_Util_String import randomstring
      >>> print randomstring(20)
      aXyGpX1bXx9IqTwF9JjT
    """

    return ''.join(random.choice(chars) for _ in range(size))


class TestRandomString(unittest.TestCase):
    def test_one(self):
        size = 10
        length = 20
        for i in range(size):
            astr = randomstring(length)
            self.assertEqual(20, len(astr))


"""
A util funciton for url join, add base url & path, also normalize the url.
:Time_Created: 2014.7.16

"""


from urlparse import urljoin
from urlparse import urlparse
from urlparse import urlunparse
from posixpath import normpath


def urljoin(base, url):
    url1 = urljoin(base, url)
    arr = urlparse(url1)
    path = normpath(arr[2])
    return urlunparse((arr.scheme,
                       arr.netloc, path, arr.params, arr.query, arr.fragment))


class TestUrlJoin(unittest.TestCase):
    def test_jion(self):
        self.assertEqual("http://www.baidu.com/abc.html",
                         urljoin("http://www.baidu.com", "abc.html"))
        self.assertEqual("http://www.baidu.com/abc.html",
                         urljoin("http://www.baidu.com", "/../../abc.html"))
        self.assertEqual("http://www.baidu.com/abc.html",
                         urljoin("http://www.baidu.com/xxx",
                                 "./../../abc.html"))
        self.assertEqual("http://www.baidu.com/abc.html",
                         urljoin("http://www.baidu.com",
                                 "abc.html?key=value&m=x"))


if __name__ == "__main__":
    unittest.main()
