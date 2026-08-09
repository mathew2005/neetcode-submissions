class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True: 
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow  == fast:
                break

        slow = 0 
        while True:
            if fast == slow: 
                return fast
            slow = nums[slow]
            fast = nums[fast]
