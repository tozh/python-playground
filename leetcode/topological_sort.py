from collections import deque
from queue import Queue

class Graph:
    def __init__(self, v):
        self.V = v
        # 每个node的入度
        self.in_degree = [0 for _ in range(self.V)]
        # 入度为0的集合
        self.dq = deque([])
        # 邻接表
        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, v1, v2):
        self.adj[v1].append(v2)
        self.in_degree[v2]+=1

    def topo_sort(self):
        for v in range(self.V):
            if self.in_degree[v]==0:
                self.dq.append(v)

        # print(self.dq)
        count = 0
        while len(self.dq) != 0:
            v = self.dq.popleft()
            print(v)
            count += 1
            for w in self.adj[v]:
                self.in_degree[w]-=1
                if self.in_degree[w]==0:
                    self.dq.append(w)
            # print(self.dq)

        if count<self.V:
            return False
        else:
            return True

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    print(g.in_degree)
    print(g.adj)
    print(g.topo_sort())



