class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxSeq = 0
        for num in nums:
            if num - 1 not in numsSet:
                seq = 0
                while num in numsSet:
                    seq += 1
                    num += 1
                maxSeq = max(seq, maxSeq)

        return maxSeq