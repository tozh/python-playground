# import Queue
# class Solution(object):
#     def updateBoard(self, board, click):
#         """
#         :type board: List[List[str]]
#         :type click: List[int]
#         :rtype: List[List[str]]
#         """
#         x = click[0]
#         y = click[1]
#         r = len(board)
#         if r == 0:
#             return board
#         c = len(board[0])
#         if c == 0:
#             return borad

#         if board[x][y]=='M':
#             board[x][y] = 'X'
#             return board
#         elif board[x][y] == 'E':
#             q = Queue.Queue(maxsize=r*c)
#             q.put((x, y))
#             while not q.empty():
#                 i ,j = q.get()
#                 neigh = [(x, y) for x in (i-1, i, i+1) for y in (j-1, j, j+1) if 0<=x<r and 0<=y<c]
#                 mine_num = 0
#                 for x, y in neigh:
#                     if board[x][y] == 'M':
#                         mine_num += 1
#                 if mine_num == 0:
#                     board[i][j] = 'B'
#                     for x, y in neigh:
#                         if board[x][y]=='E':
#                             q.put((x, y))
#                 else:
#                     board[i][j] = str(mine_num)
#         return board

import queue


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        r = len(board)
        if r == 0:
            return board
        c = len(board[0])
        if c == 0:
            return board

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        elif board[click[0]][click[1]] == 'E':
            q = queue.Queue(maxsize=r * c)
            q.put(click)
            while not q.empty():
                i, j = q.get()
                mine_num = 0
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        if 0 <= x < r and 0 <= y < c:
                            if board[x][y] == 'M':
                                mine_num += 1

                if mine_num == 0:
                    board[i][j] = 'B'
                    for x in (i - 1, i, i + 1):
                        for y in (j - 1, j, j + 1):
                            if 0 <= x < r and 0 <= y < c:
                                if board[x][y] == 'E':
                                    q.put((x, y))
                else:
                    board[i][j] = str(mine_num)
        return board

a = [["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]
click = [0,0]
s = Solution()
s.updateBoard(a, click)
print(a)