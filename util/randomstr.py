import string
import random

"""
random string generator
~~~~~~~~~~

A util function to generate random string for given length & charset.

:Time_Created: 2014.7.15

"""


def str_generator(size=6,
                  chars=string.ascii_uppercase + string.ascii_lowercase
                  + string.digits):

    """Constructs random string with given size & charset
    Returns :class:`String<String>` object.

    :param size: (optional) desired length of string.
    :param chars: (optional) charset from which string is chosen.

    Usage::

      >>> from randomstr import str_generator
      >>> size = 10
      >>> length = 20
      >>> for i in range(size):
              print str_generator(length)
      GmsrkvBDt4OhRQnckHwa
      0FaXzpare3GI3lQuv16M
      UpedQkz14QOZGfMAV3F6
      apHF8rOCsbAYHKvdvEpn
      2PmTuuHDXCTxtiakONQ7
      uo9skXMHBY3Lpe3lll4O
      PFDGxxBxrvML1aNjeZgs
      1cp8sOSb9QII0T9rNx5M
      M5wY5pt44JMw6XlKL88A
      aXyGpX1bXx9IqTwF9JjT
    """

    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    size = 10
    length = 20
    for i in range(size):
        print str_generator(length)
