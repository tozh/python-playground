from itertools import dropwhile, count, cycle
import random


c = count()

print c
print random.randint(1, int(1. / 0.5))
# print next(dropwhile(lambda _: random.randint(1, int(1. / 0.5)) == 1, c))
print list(dropwhile(lambda e: e<2, c))