class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # input: sorted (ascending) list, target
        # output: int (index of target in the list) or -1 (if doesn' exist
        # must be O(logn)-> time
        # edge cases: one el, -1, 
        # [1]
        if nums[0] == target:
            return 0
        l,r = 0, len(nums) - 1

        while l < r - 1:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m
            
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        return -1
        """
        Input: nums = [-1,0,2,4,6,8], target = 3
                       l    m     r
                            l r => (either check if l and r diff is only 1 or l or r == mid before setting it, and also checking if value is == l or r pointer)
                            m
        """

        