# mask = (1<<4)-1
# i = mask
# while i!=0 :
#     i = (i-1)&mask
#     print(i)
import random


def naive(a):
    for j in range(0, 31):
        if (a >> j) & 1 == 1:
            return j
    return 32


def binary(a):
    n = 16
    b = 0
    if a == 0:
        return 32

    while a != 0 and n>=1:
        if a & ((1 << n) - 1) != 0:
            # print 'right'
            n = n >> 1
        else:
            # print 'left'
            b += n
            a = a >> n
            n = n >> 1
    return b


for _ in range(0, 100):
    a = random.randint(0, 2**32-1)
    print(a, ': ', naive(a) , binary(a))

# a = 1<<16
# print a, ': ', naive(a) , binary(a)