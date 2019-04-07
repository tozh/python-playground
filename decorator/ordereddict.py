from collections import OrderedDict

od = OrderedDict()
for i in range(10):
    od[i] = i
od.pop(0)
od[10] = 10
print(next(iter(od)))
print(next(iter(od)))
od.pop(1)

print(next(iter(od)))