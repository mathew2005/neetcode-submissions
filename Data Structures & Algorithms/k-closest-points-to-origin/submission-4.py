from heapq import heapify, heappop, heappush
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapify(minHeap)

        for x,y in points:
            dis = math.sqrt(x**2 + y**2)
            heappush(minHeap,(dis,x,y))
        res = []
        for i in range(0,k):
            temp = heappop(minHeap)
            res.append([temp[1], temp[2]])
        
        return res