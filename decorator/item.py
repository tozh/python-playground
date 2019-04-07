class Foo:
    def __init__(self, list=None):
        if not list:
            self.list = []
        else:
            self.list = list

    def __getitem__(self, key):
        return self.list[key]

    def __setitem__(self, key, val):
        self.list[key] = val

    def __bool__(self):
        return len(self.list) != 0

    def __setslice__(self, i, j, sequence):
        return self.list[i:j:sequence]

    def append(self, val):
        self.list.append(val)

    def __repr__(self):
        return self.list.__repr__()


foo = Foo([0, 1, 2, 3, 4])
foo.append(5)
foo[0] = 999
print(foo)
