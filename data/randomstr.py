import string
import random

def str_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__=="__main__":
    count  = 10
    length = 20
    for i in  range(count):
        print str_generator(length)
