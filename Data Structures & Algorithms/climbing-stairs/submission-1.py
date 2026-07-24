class Solution:
    def climbStairs(self, n: int) -> int:
        # input: int
        # output: int

        memo = {n: 1, n+1:0}
        
        

        def climb(curr):
            nonlocal memo
            if curr in memo:
                return memo[curr]
            else:
                memo[curr] = climb(curr + 1) + climb(curr + 2)
                return memo[curr]

        return climb(0)
