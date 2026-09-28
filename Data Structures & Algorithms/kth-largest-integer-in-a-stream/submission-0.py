from heapq import heapify, heappop, heappush
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-x for x in nums]
        heapify(self.nums)


        

    def add(self, val: int) -> int:
        heappush(self.nums,-1 * val)
        temp = list(self.nums)
        heapify(temp)
        
        for _ in range(self.k):
            res = heappop(temp)
        return -1 * res