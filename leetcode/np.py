import numpy as np

a = [1, 2, 3, 4]
def b(i, arr):
    if i<len(arr):
        arr = arr[:]
        if arr[i]>2:
            arr[i] = -1
        b(i+1, arr)
    else:
        print(arr)
        return

b(0, a)
print(a)