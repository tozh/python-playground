def fib_generator(largest):
    a, b = 0, 1
    counter = 0
    while counter < largest:
        a, b = b, a+b
        counter += 1
        yield a


def infinite_fib_generator():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a


# for i, n in enumerate(fib_generator(20)):
#     print(i, n)
# for i, n in enumerate(infinite_fib_generator()):
#     if i < 40:
#         print(i, n)
#     else:
#         break


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

fib = Fib()
fib_iter = iter(fib)
for i, n in enumerate(fib):
    if i < 40:
        print(i, n)
    else:
        break
