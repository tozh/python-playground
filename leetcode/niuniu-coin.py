import sys
import copy

def c(k, x, p):
    if k <= -1:
        return 0
    elif x <= 0:
        return 0
    else:
        return max(1+c(k-1, x-p[k], p), c(k-1, x, p))

if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip().split(' ', 1)
    n = int(line1[0])
    s = int(line1[1])
    p = [int(pk) for pk in sys.stdin.readline().strip().split(' ')]
    f = [True for i in range(n)]
    print(c(n-1, s, p))

# 5 9
# 4 3 1 5 4