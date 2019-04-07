def quickSort(num, l, r):
    if l>=r:
        return
    print(num[l: r+1])
    p = num[l]
    i = l
    j = r
    while i<j:
        while i<j and num[j]>=p:
            j -= 1
        if i<j:
            num[i] = num[j]
            i+=1
        while i<j and num[i]<=p:
            i += 1
        if i<j:
            num[j] = num[i]
            j-=1

    num[i] = p
    quickSort(num, l, i-1)
    quickSort(num, i+1, r)

a = [2,9,6,3]

quickSort(a, 0, len(a)-1)
print(a)