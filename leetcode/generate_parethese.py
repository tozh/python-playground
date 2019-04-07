class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.n = n
        self.generate("", 0, 0)
        return self.result

    def generate(self, string, left, right):
        if left == right:
            self.generate(string+'(', left+1, right)
        if left > right:
            if left < self.n:
                self.generate(string+'(', left+1, right)
            if right < self.n:
                self.generate(string+')', left, right+1)
        if right == self.n:
            self.result.append(string)

s = Solution()
s.generateParenthesis(3)