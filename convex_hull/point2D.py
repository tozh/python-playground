
class Point2D:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        else:
            return self.y.__lt__(other.y)

    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        else:
            return self.y.__le__(other.y)

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x < other.x:
            return False
        else:
            return self.y.__gt__(other.y)

    def __ge__(self, other):
        if self.x > other.x:
            return True
        elif self.x < other.x:
            return False
        else:
            return self.y.__ge__(other.y)

    def __hash__(self):
        return self.__str__().__hash__()

    def __eq__(self, other):
        return self.x == other.x and self.y==other.y


if __name__ == '__main__':
    n1 = Point2D(2, 0)
    n2 = Point2D(1, 0)
    print(n2>n1)