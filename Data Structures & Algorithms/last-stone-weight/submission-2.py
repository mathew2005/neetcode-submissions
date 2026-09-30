from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: 
        if len(stones) <= 1: return stones[0]
        stones = [-x for x in stones]
        heapify(stones)
        
        while len(stones) > 1:
            f =  heappop(stones)
            s =  heappop(stones)
            if f == s:
                continue
            elif f < s:
                heappush(stones,(f-s))
            else:
                heappush(stones,(s-f))
        
        return stones[0] * -1 if stones else 0