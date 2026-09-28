from heapq import heapify, heappop, heappush
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = Counter(s)
        res = []
        maxHeap = [(-freq,char) for char,freq in freqMap.items()]
        heapify(maxHeap)
        prev = None
        
        while maxHeap:
            temp = None
            if prev == maxHeap[0][1]:
                temp = heappop(maxHeap)
            
            if not maxHeap:
                return ""
            
            freq, char = heappop(maxHeap)
            res.append(char)

            if freq + 1 < 0:
                heappush(maxHeap, (freq + 1, char))
            prev = char
            if temp:
                heappush(maxHeap,temp)
        
        return "".join(res)