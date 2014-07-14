import string
import random


# a tool stript for random string as test data
# input factors:
# size, length, charset

def str_generator(size=6,
                  chars=string.ascii_uppercase + string.ascii_lowercase
                  + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    size = 10
    length = 20
    for i in range(size):
        print str_generator(length)
