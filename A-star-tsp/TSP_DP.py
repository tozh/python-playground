from AStar import AStar
import sys


class TSP_DP:
    def __init__(self, a):
        self.nodes, self.mat = a.nodes, a.mat
        self.len = len(self.nodes) if self.nodes != -1 else 0

    def opt(self, node_list, k):
        if self.nodes == -1:
            return -1

        if sum(node_list) == 3:
            index = node_list.index(1, 1)  # find the second 1 in the list (s-1, t-1 and the only node-1)
            return self.mat[index][0]

        # V-k
        node_list[k] = 0

        _min = 99999
        for j in range(1, self.len-1):
            if node_list[j] == 1:  # j in V-k
                sep = self.opt(node_list[:], j)  # opt(V-k, j)
                temp = sep + self.mat[j][k]
                _min = temp if _min > temp else _min
        return _min

    def do_DP(self):
        node_list = [1] * self.len

        if self.len == 2:
            return self.mat[0][1]
        else:
            _min = 1000000
            for k in range(1, self.len-1):
                value = self.opt(node_list[:], k)
                if value == -1:
                    return -1
                else:
                    temp = value + self.mat[k][-1]
                    _min = temp if _min>temp else _min

            return _min


# if __name__ == '__main__':
#     a = AStar()
#     tsp_dp = TSP_DP(a)
#     print('final: ' + str(tsp_dp.find_first_node()))






