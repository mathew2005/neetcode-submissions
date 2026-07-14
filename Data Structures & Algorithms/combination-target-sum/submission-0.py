class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # input: list of distinct int, target int
        # output: list of all comb of nums that sum to target

        # same number can be chosen unlimited times
        # same if the freq of chosen numbers is the same, if not they are d/t

        # order doesn't matter both for combination of el and the list of the combination
        nums.sort()
        result = []
        # edge cases: nums[i] > target, 
        def backtrack(index: int, numsSum: List[int]):
            
            if sum(numsSum) == target:
                result.append(numsSum[:])
                return
                
            # base case: 
                # when the sum of all comb > target
            if sum(numsSum) > target:
                return
            if index == len(nums):
                return

            
            # add current index to nums
            numsSum.append(nums[index])
            backtrack(index,numsSum)
            numsSum.pop()

            # move to the next index to nums
            backtrack(index+1, numsSum)
            
            
        backtrack(0, [])
        return result
        