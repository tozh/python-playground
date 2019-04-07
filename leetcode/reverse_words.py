s = "the sky is blue"

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = " ".join(s.split(" ")[::-1])
        print(a, len(a), a=="")
        return " ".join(s.split(" ")[::-1])

solu = Solution()
solu.reverseWords("")


b = " "
print (b.split(" "))