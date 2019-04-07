import random
import math
from itertools import dropwhile, count, cycle
from abc import ABCMeta, abstractmethod, abstractproperty


def geometric(p):
    return (next(dropwhile(lambda _: random.randint(1, int(1. / p)) == 1, count())) for _ in cycle([1]))

class NIL(object):
    def __cmp__(self,other):
        return 1

    def __str__(self):
        return 'NIL'

    def __nonzero__(self):
        return False

class Level(object):
    def __init__(self, forward=None, span=0):
        self.forward = forwards
        self.span = span

class _SkipListNode(object):
    def __init__(self, score=0, obj=None, backward=None, forward=None):
        self.score = score
        self.obj = obj
        self.backward = backward
        self.forward = forward
        self.__generate_levels()

    def __generate_levels(self):
        for level in range(len(self.backward)):
            self.backward[level].forward[level] = self.forward[level].backward[level] = self

class SkipListBase(object):
    __metaclass__ = ABCMeta


    @abstractproperty
    def head(self):
        raise NotImplementedError

    @abstractproperty
    def tail(self):
        raise NotImplementedError





