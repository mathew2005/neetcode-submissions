from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap, sortedFreq, res = Counter(nums), [[] for _ in range(len(nums))], []
        for value, freq in freqMap.items(): sortedFreq[freq - 1].append(value)
        for i in range(len(sortedFreq) - 1, -1, -1):
            if len(res) == k:
                break
            if sortedFreq[i]:
                res.extend(sortedFreq[i])

        return res