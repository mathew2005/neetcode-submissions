from heapq import heapify, heappush, heappop
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closeheap = []
        heapify(closeheap)

        for point in points: 
            x,y = point
            distance = math.sqrt(((x**2) + (y**2)))
            if len(closeheap) < k:
                heappush(closeheap,(-distance,x,y))
            elif -distance > closeheap[0][0]:
                heappop(closeheap)
                heappush(closeheap,(-distance,x,y))
        res = []
        for distance,x,y in closeheap:
            res.append([x,y])
        return res

