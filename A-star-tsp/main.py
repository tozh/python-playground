from AStar import AStar
from TSP_DP import TSP_DP
from TSP_SA import TSP_SA

import time

a = AStar()
print(len(a.nodes))
start1 = time.clock()

print('Choose SA: ')
tsp_sa = TSP_SA(a)
print(tsp_sa.do_SA())

end1 = time.clock()

print('SA time :' + str((end1 - start1)) + 's')

start2 = time.clock()

print('Choose DP: ')
tsp_dp = TSP_DP(a)
print(tsp_dp.do_DP())

end2 = time.clock()

print('DP time :' + str((end2 - start2)) + 's')







