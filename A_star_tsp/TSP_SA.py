from AStar import AStar
import sys
import random
import math



class TSP_SA:
    def __init__(self, a):
        self.nodes, self.mat = a.nodes, a.mat
        self.len = len(self.nodes) if self.nodes != -1 else -1

    def generate_new_solution(self, old):
        k = random.randint(1, self.len-2)
        m = random.randint(1, self.len-2)
        _old = old[:]
        while m == k:
            m = random.randint(1, self.len-2)
        _old[k], _old[m] = _old[m], _old[k]
        return _old

    def target_function(self, solution):
        result = 0
        for i in range(1, self.len):
            result += self.mat[solution[i]][solution[i-1]]
        return result

    def do_SA(self):
        if self.len == -1:
            # return -1, -1, -1, -1
            return -1

        x_0 = [i for i in range(self.len)]
        t_0 = 50 * self.len
        x_i = x_0
        t = t_0
        min_t = 0.01

        descending_rate = 0.98
        inner_loop_times = 40 * self.len
        # print('inner_loop_times: ' + str(inner_loop_times))
        outer_loop_time = 0
        f_x_i = self.target_function(x_i)
        best_x = x_i
        best_value = f_x_i

        while t >= min_t:
            # print('outer_loop_time: ' + str(outer_loop_time))
            outer_loop_time += 1
            for N in range(inner_loop_times):
                x_j = self.generate_new_solution(x_i)  # generate new solution
                f_x_j = self.target_function(x_j)
                if f_x_j < best_value:
                    best_x = x_j
                    best_value = f_x_j

                delta_f = f_x_j - f_x_i

                if delta_f < 0:  # accept new solution x_j
                    x_i = x_j
                    f_x_i = f_x_j
                else:
                    p = math.exp(-delta_f/t)
                    if p > random.uniform(0,1):  # accept new solution x_j
                        x_i = x_j
                        f_x_i = f_x_j

            t *= descending_rate
            # print('t: ' + str(t))

        # return best_x, best_value, x_i, f_x_i
        return best_value, f_x_i

# if __name__ == '__main__':
    # print(math.exp(10/0.1))
    # a = AStar()
    # tsp_sa = TSP_SA(a)
    # best_x, best_value, x, f_x = tsp_sa.do_SA()
    # print(best_x)
    # print(best_value)
    # print(tsp_sa.target_function(best_x))
    # print(x)
    # print(f_x)
    # print(tsp_sa.target_function(x))










