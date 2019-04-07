def dfs(maze, n, m, i, j, end):
    maze[i][j] = '.'
    if end[0] == i and end[1] == j:
        return True
    else:
        neigh = [(x, y) for x in [i-1, i, i+1] for y in [j-1, j, j+1]
                 if 0 <= x < n and 0 <= y < m and maze[x][y]!='.']
        for en in neigh[:]:
            if maze[en[0]][en[1]] == '*':
                if (en[0], en[1]) in neigh:
                    neigh.remove((en[0], en[1]))
                if en[0] == i:
                    if (en[0], en[1]-1) in neigh:
                        neigh.remove((en[0], en[1]-1))
                    if (en[0], en[1]+1) in neigh:
                        neigh.remove((en[0], en[1]+1))
                elif en[1] == j:
                    if (en[0]-1, en[1]) in neigh:
                        neigh.remove((en[0]-1, en[1]))
                    if (en[0] + 1, en[1]) in neigh:
                        neigh.remove((en[0]+1, en[1]))
                else:
                    if (en[0], j) in neigh:
                        neigh.remove((en[0], j))
                    if (i, en[1]) in neigh:
                        neigh.remove((i, en[1]))
        for en in neigh:
            if dfs(maze, n, m, en[0], en[1], end)==True:
                return True
    return False

while True:
    s1 = raw_input()
    l1 = s1.split(' ')
    n = int(l1[0])
    m = int(l1[1])
    if s1 != '':
        maze = []
        for i in range(n):
            s = list(raw_input())
            maze.append(s)
        start = []
        end = []
        for k in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[k][j] == 'A':
                    start = (k, j)
                if maze[k][j] == 'B':
                    end = (k, j)
        if start[0] == end[1]:
            print True
        print dfs(maze, n, m, start[0], start[1], end)
    else:
        continue







