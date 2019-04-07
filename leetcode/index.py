class Solution:
    def strStr(self, T, P):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not P:
            return 0
        lt = len(T)
        lp = len(P)
        if lp > lt:
            return -1
        i = 0
        j = 0
        while i + j < lt:
            if T[i + j] == P[j]:
                j += 1
                if j == lp:
                    return i
            else:
                if i + lp >= lt:
                    return -1
                char = T[i + lp]
                found = False
                for j in range(lp - 1, -1, -1):
                    if char == P[j]:
                        found = True
                        break
                if not found:
                    i += lp + 1
                else:
                    i += lp - j
                j = 0
        return -1


p = "aairbnbxxxxxx"
t = "airbnb"
s = Solution()
print(s.strStr(p, t))