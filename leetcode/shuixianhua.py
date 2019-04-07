# line1 = input().split(" ")
# n, m = int(line1[0]), int(line1[1])
# mark = [0] * n
# into = [0] * n
# edges = [[0 for i in range(n)]for j in range(n)]
# for i in range(m):
#     line = input().split(" ")
#     u, v = int(line[0])-1, int(line[1])-1
#     if edges[u][v] == 1 or u == v:
#         continue
#     edges[u][v] = 1
#
# count = 0
# for k in into:
#     if k > 0:
#         count += 1
# print(count)
#
# def dfs(start):
#     li = [start, ]
#     for k in range(n):
#         edges[start,]
#     for node in li:
#
#         if mark[node] == 0:
#             mark[start] = 1
#             dfs(node)
#             mark[start] = 0
#
# def judge(a, b, c):
#     for m in range(b+1):
#         if a * m % b == c:
#             return True
#     return False
#
# t = int(input())
# out = []
# for _ in range(t):
#     line = input().split(" ")
#     a, b, c = int(line[0]), int(line[1]), int(line[2])
#     if judge(a, b, c):
#         out.append('YES')
#     else:
#         out.append('NO')
# for s in out:
#     print(s)

def gcd(a, b):
    while b > 0:
        c = a
        a = b
        b = c%b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmN(s , t):
    l = s
    for i in range(s, t+1):
        l = lcm(i, l)
    return l
import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % 2 == 0:
            return False
    return True

def A(n):
    if is_prime(n):
        return 2 * n
    else:
        for i in range(n, 1, -1):
            if is_prime(i):
                return 2*i
def B(n):
    m = n+1
    while True:
        if lcmN(n+1, m) == lcmN(1, m):
            break
        m+=1
    return m


for n in range(1, 1000):
    print(n, "------>", A(n), B(n), A(n) == B(n))