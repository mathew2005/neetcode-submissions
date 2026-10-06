from collections import Counter, deque
from heapq import heapify, heappush,heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap, maxHeap = Counter(tasks), []
        heapify(maxHeap)
        for char,freq in freqMap.items(): heappush(maxHeap,(-freq,char))
        t, q = 0, deque([])
        while maxHeap or q:
            if maxHeap:
                freq, char = heappop(maxHeap)
                freq += 1
                if freq < 0:
                    q.append((t + n,freq,char))
            
            if q and q[0][0] == t:
                tn, freq, char = q.popleft()
                heappush(maxHeap,(freq, char))
            t += 1
        return t