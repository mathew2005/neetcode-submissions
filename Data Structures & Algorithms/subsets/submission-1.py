class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums (unique int)
        # output: possible set of nums
        # solution set(must not contain duplicate subsets)
        # order doesn't matter
        # empty set is a subset of every set
        result = []
        def backtracking(path, index):
            
            if len(nums) == index:
                result.append(path[:])
                return
            
            # case 1: (add element to the set)
            path.append(nums[index])
            backtracking(path, index+1)
            path.pop()

            # case 2: (don't add element to the set)
            backtracking(path, index + 1)

        backtracking([], 0)
        return result