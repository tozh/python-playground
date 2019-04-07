while True:
    S = raw_input()
    T = raw_input()

    def num(a, b):
        res = 0
        for i in range(len(b)):
            if a[i]!=b[i]:
                res += 1
        return res

    def dp(s, t):
        lt = len(t)
        ls = len(s)
        res = 0
        for i in range(0, ls - lt):
            res += num(s[i:i+lt], t)

        return res


    print dp(S, T)
