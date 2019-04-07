def append_list(a):
    def append(item):
        a.append(item)
        return a
    return append
a = [1, 2, 3]
func = append_list(a)
func(4)
func(5)

arr = [3 for _ in range(10)]
for i in range(len(arr)-1, 0, -1):



print(func(5))