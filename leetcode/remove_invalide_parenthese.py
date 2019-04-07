class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        level = [s, ]
        while True:
            valid = [string for string in level if self.is_valid(string)]
            if valid:
                return valid
            next_level = []
            for string in level:
                if len(string) == 1:
                    next_level.append("")
                for i in range(1, len(string)):
                    if i == 1 or string[i] != string[i - 1]:
                        next_level.append(string[:i] + string[i + 1:])
            level = next_level

    def is_valid(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            if s[i] == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0


s = Solution()
print(s.removeInvalidParentheses("))"))