class Meta(type):
    # def __new__(cls, *args, **kwargs): # new Meta self instances
    #     return super().__new__(*args, **kwargs)

    def __init__(cls, *args, **kwargs):  # init Meta self instances
        cls.instances = [None, None]
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.instances[0] is None:
            cls.instances[0] = super().__call__(*args, **kwargs)
            return cls.instances[0]
        if cls.instances[1] is None:
            cls.instances[1] = super().__call__(*args, **kwargs)
        return cls.instances[1]


class People(metaclass=Meta):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello! My name is %s." % self.name)

a = People("Tom")
b = People("Jerry")
c = People("Jack")

a.introduce()
b.introduce()
c.introduce()
print(id(a), id(b), id(c))