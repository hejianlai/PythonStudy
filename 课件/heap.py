import heapq
import random

heap = []
data = list(range(10000))
random.shuffle(data)
# for num in data:
#     heapq.heappush(heap, num)
# for i in range(len(heap)):
#     print(heapq.heappop(heap))
print(heapq.nsmallest(10, data))


