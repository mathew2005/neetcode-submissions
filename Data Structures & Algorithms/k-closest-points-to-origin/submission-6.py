from heapq import heapify, heappop, heappush
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dis = math.sqrt(x**2 + y**2)
            minHeap.append((dis,x,y))
        
        heapify(minHeap)
        res = []
        for i in range(0,k):
            dist,x,y = heappop(minHeap)
            res.append([x,y])
        
        return res