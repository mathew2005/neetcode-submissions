class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, index):

            # base case (when index is at the end of the list)
            if index > len(nums) - 1:
                result.append(path[:])
                return

            # adding index to path -> no
            backtrack(path, index + 1)
            # adding index to path -> yes
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()

       
        backtrack([], 0)
        
        return result