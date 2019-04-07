start = 199
end = 600000
X = 3
Y = 100
Z = 1
l = [10000000000 for _ in range(start, end<<1)]
l[0] = 0

def dp(x):
    return l[x-start]

def set_dp(x, l, val):
    l[x-start] = val

def odd(x):
    return  x&1 == 1

def even(x):
    return x&1 == 0

def my_min(a, b):
    return a if a <= b else b

def main():
    if even(start):
        for x in range(start+2, end-1, 2):
            if even(x>>1) and x>>1>=start:
                set_dp(x, l, min(dp(x-2)+X, dp(x>>1)+Y))
            else:
                set_dp(x, l, dp(x-2)+X)

        for x in range((end << 1)-3, end + 1, -2):
            if even(x>>1):
                set_dp(x, l, min(dp(x+2)+Z, dp(x>>1)+Y))
            else:
                set_dp(x, l, dp(x+2)+Z)

        set_dp(end, l, min(dp(end-2)+X, dp(end+2)+Z, dp(end>>1)))

    else:
        for x in range(start+2, end-1, 1):
            if x >> 1 >= start:
                set_dp(x, l, min(dp(x - 2) + X, dp(x >> 1) + Y))

        for x in range((end << 1)-3, end + 1, -1):
                set_dp(x, l, min(dp(x + 2) + Z, dp(x >> 1) + Y))

        set_dp(end, l, min(dp(end - 2) + X, dp(end + 2) + Z, dp(end >> 1)+Y))
main()

print(dp(end))
# print(dp(end >> 1))
# print(dp(end + 2))
# print(dp(end - 2))









# def help(t):
#     if t<start or t>(end<<1):
#         return 1000000000000
#     elif t==start:
#         return 0
#     elif t<end-1:
#         if odd(t):
#             return help(t-2)+x
#         else:
#             return min(help(t-2)+x, help(t//2)+y)
#     elif end-1<=t<=end+1:
#         if odd(t):
#             return min(help(t-2)+x, help(t+2)+z)
#         else:
#             return min(help(t-2) + x, help(t+2) + z, help())
#     else:  # end < x < end<<1
#         if odd(t):
#             return help(t+2) + z
#         else:
#             return min(help(t-2)+z, help(t+2)+z, help(t//2)+y)

# def main():
#     print(help(end))
#
# main()