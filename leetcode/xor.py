class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        tran = dict()
        state = 0
        i = 0
        while i < len(p):
            if i + 1 < len(p) and p[i + 1] == "*":
                tran[(state, "")] = state + 1
                tran[(state + 1, p[i])] = state + 1
                tran[(state + 1, "")] = state + 2
                state += 2
                i += 2
            else:
                tran[(state, p[i])] = state + 1
                state += 1
                i += 1

        matched = state


        cur_state = [0]
        next_state = set()
        i = 0

        while i < len(s):
            c = s[i]
            tail = max(cur_state)
            while (tail, '') in tran:
                cur_state.add(tail + 1)
                tail += 1
            for state in cur_state:
                for token in (c, '.'):
                    if (state, token) in tran:
                        next_state.add(tran[(state, token)])

            cur_state = next_state
            next_state = set()
            i += 1

        if len(p) and p[-1] == '*':
            for k in (1, 2):
                if (matched-k) in cur_state:
                    return True
            return False
        return matched in cur_state

s = "a"
p = "ab*"
solution = Solution()
print(solution.isMatch(s, p))