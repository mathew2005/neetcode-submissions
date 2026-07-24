class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # down or right
        # top left to bottom right
        # output: int (num of ways to traverse through the grid)

        memo = {(m-1,n-1): 1}
        
        def paths(r,c):
            nonlocal m
            nonlocal n

            if r > m-1 or c > n-1:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]
            
            else:
                memo[(r,c)] = paths(r+1,c) + paths(r,c+1)
                return memo[(r,c)]
        paths(0,0)

        return memo[(0,0)]