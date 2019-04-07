import random

print(random.randint(1, 2))
a = list(range(1, 10))

# for i in range(len(a)-1, 0, -1):
#     p = random.randint(0, i)
#     a[i], a[p] = a[p], a[i]

result = a[:]
for i in range(0, len(a)):
    j = random.randint(0, i)
    result[i] = result[j]
    result[j] = a[i]
print(a)
print(result)