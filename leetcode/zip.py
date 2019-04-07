class Solution(object):
    def maximalSquare(self, matrix):
        """
  :type matrix: List[List[str]]
  :rtype: int
  """
        r = len(matrix)
        if r == 0:
            return 0
        l = len(matrix[0])
        if l == 0:
            return 0

        opt = [[0] * l for _ in range(r)]

        if_one = False
        for j in range(l):
            opt[0][j] = matrix[0][j]
            if opt[0][j] == 1:
                if_one = True

        for i in range(r):
            opt[i][0] = matrix[i][0]
            if opt[i][0] == 1:
                if_one = True

        max_ever = 1 if if_one else 0

        for i in range(1, r):
            for j in range(1, l):
                if matrix[i][j] == 0:
                    opt[i][j] = 0
                else:
                    opt[i][j] = min(opt[i - 1][j], opt[i][j - 1], opt[i - 1][j - 1]) + 1
                    max_ever = max(opt[i][j], max_ever)
        return max_ever
