class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 0 -> water, 1 -> land
        # island -> hor or ver 1 connected
        # assumption: four edges of the grid -> 0
        # q : is island 1s surrounded by 0s ?
        # return -> max area of an island in grid
        # no island -> return 0

        # area -> number of grids in the island

        
        # edge cases: [[]], [[0,0,0]], [[1,1,1]], 

        # keep track of visited places
        # time complexity: O(r.c * r.c)
        # space complexity: O(r.c)
        
        visited = set()  
        maxArea = 0
        def dfs(r,c):
            if grid[r][c] == 1 and (r,c) not in visited:
                up, down, left, right = (r-1,c), (r+1, c), (r,c-1), (r,c+1)
                nonlocal currArea 
                currArea += 1

                visited.add((r,c))  
                if up[0] >= 0:
                    dfs(*up)
                
                if down[0] <= len(grid) - 1:
                    dfs(*down)
                
                if left[1] >= 0:
                    dfs(*left)
                
                if right[1] <= len(grid[0]) - 1:
                    dfs(*right)
            else:
                return 0
                
                

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == 1 and (r,c) not in visited:
                    currArea = 0

                    dfs(r,c)
                    maxArea = max(maxArea, currArea)

        
        return maxArea