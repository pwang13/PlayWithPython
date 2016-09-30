from __future__ import division
import random

def random_odd_(start = 1, end = 1000, count = 20):
    for i in xrange(count):
        x = random.randint(0, end * 2)
        x = int(x / 2)
        x = x + 1 if x % 2 == 0 else x
        yield x


print(list(random_odd_()))
