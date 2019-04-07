# def singleton(cls):
#     _instances = dict()
#
#     def wrapper(*args, **kwargs):
#         print(_instances)
#         if cls not in _instances:
#             _instances[cls] = cls(*args, **kwargs)
#         return _instances[cls]
#     return wrapper
#
#
# @singleton
# class People(object):
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print("Hello! My name is %s." % self.name)
#
# @singleton
# class Human(object):
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print("Hello! My name is %s." % self.name)
#
#
# a = People("Tom")
# b = People("Jerry")
# c = People("Jack")
#
# a.introduce()
# b.introduce()
# c.introduce()
# print(id(a), id(b), id(c))
#
# a1 = Human("Tom")
# b1 = Human("Jerry")
# c1 = Human("Jack")
#
# a1.introduce()
# b1.introduce()
# c1.introduce()
# print(id(a1), id(b1), id(c1))


class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):

        if not cls._instance:
            cls._instance = super().__call__(*args, *kwargs)
        return cls._instance


class People(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello! My name is %s." % self.name)


class Human(metaclass=SingletonMeta):
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

c1 = Human("Jack")
a1 = Human("Tom")
b1 = Human("Jerry")

a1.introduce()
b1.introduce()
c1.introduce()
print(id(a1), id(b1), id(c1))