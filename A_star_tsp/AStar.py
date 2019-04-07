
import heapq
import os
import os.path
import sys
from node import Node


class AStar:
    def __init__(self):
        # self.maze = self.read_maze(filepath=sys.argv[1])
        self.maze = self.read_maze(filepath='maze.txt')
        self.w, self.h = len(self.maze[0]), len(self.maze)
        self.nodes, self.mat = self.dist_matrix()

    def read_maze(self, **kwargs):

        if 'filepath' in kwargs.keys():
            file = open(kwargs['filepath'], 'r')
            lines = file.readlines()
            maze = []

            for i, line in enumerate(lines):
                if i == 0:
                    words = line.split(' ')
                else:
                    nds = list(line.strip())
                    maze.append(nds)
            return maze
        elif 'maze' in kwargs.keys():
            return kwargs['maze']

    def __str__(self):
        return self.maze.__str__()

    def find_path(self, s, t):
        # s, t = self.find_s_t()

        if s[0] == t[0] and s[1] == t[1]:
            return 0

        s = Node(s[0], s[1])
        t = Node(t[0], t[1])
        # print('s: ' + str(s))
        # print('t: ' + str(t))
        closed = set()
        open = []
        heapq.heappush(open, s)
        while len(open) != 0:
            n = heapq.heappop(open)
            # print(n)
            closed.add(n)

            # neighbors = [Node(x,y,node_type, g, f) for all x, y that are valid]
            neighbors = [Node(_x, _y, n.g+1, n.g+1+self.get_h(_x, _y, t))
                         for (_x, _y) in [(n.x-1, n.y), (n.x+1, n.y), (n.x, n.y-1), (n.x, n.y+1)]
                         if self.maze[_x][_y] is not '#'
                         ]

            for neighbor in neighbors:
                if neighbor == t:  # found the shortest path
                    return neighbor.g

                if neighbor not in closed:
                    if neighbor not in open:
                        heapq.heappush(open, neighbor)
                    else:  # check if update g and father as n
                        index = open.index(neighbor)
                        if open[index].g > neighbor.g:  # need update the f,g fro the node
                            open[index] = neighbor
                            heapq.heapify(open)
        return -1

    def get_h(self, x, y, t):
        '''
        get the length from (x,y) to destination |x1-x2| + |y1-y2|
        :param p:
        :param dest:
        :return:
        '''

        return abs(x-t.x) + abs(y-t.y)


    def find_all_nodes(self):
        for line in self.maze:
            print(line)
        s = []
        t = []
        at = []
        for i, r in enumerate(self.maze):
            for j, ch in enumerate(r):
                if ch == 'S':
                    s.append((i, j))

                elif ch == 'G':
                    t.append((i, j))
                elif ch == '@':
                    at.append((i, j))
        return s, t, at

    def dist_matrix(self):
        s, t, at = self.find_all_nodes()
        nodes = s + at + t
        mat = []
        for i in range(len(nodes)):
            dists = []
            for j in range(i): # 0i, 1i, 2i... i-1)i
                dist = self.find_path(nodes[j], nodes[i])
                if dist == -1:
                    return -1, -1
                dists.append(dist)
                mat[j].append(dist)
            dists.append(0)
            mat.append(dists)
        return nodes, mat


if __name__ == '__main__':
    a = AStar()
    for line in a.maze:
        print(line)
    # print(a.find_path())
    nodes, mat = a.dist_matrix()

    # n1 = Node(1,1, '@', 1, 10)
    # n2 = Node(1,1, '@', 3, 18)
    # print(n1>n2)


