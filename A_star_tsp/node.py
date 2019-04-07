class Node:
    def __init__(self, x, y, g=0, f=0):
        self.x = x
        self.y = y
        self.g = g
        self.f = f

    def __lt__(self, other):
        return self.f.__lt__(other.f)

    def __le__(self, other):
        return self.f.__lt__(other.f)

    def __gt__(self, other):
        return self.f.__gt__(other.f)

    def __ge__(self, other):
        return self.f.__ge__(other.f)

    def __eq__(self, other):
        return (self.x, self.y).__eq__((other.x, other.y))

    def __ne__(self, other):
        return (self.x, self.y).__ne__((other.x, other.y))

    def __hash__(self):
        return (self.x, self.y).__hash__()

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'




