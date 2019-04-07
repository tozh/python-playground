a = [2, 4,5,6,7,31,1,3]
print(len(a))
import heapq

heapq.heapify(a)
heapq.heappush(a, 8)
print(len(a))