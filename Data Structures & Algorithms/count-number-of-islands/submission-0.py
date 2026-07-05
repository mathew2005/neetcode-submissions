class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input: 2d grid, '1' is land and '0' is water
        # output: number of islands
        # island -> adj 1 connected hor/vert surrounded by 0
        # assumption: outside (edge of grid) is surrounded by 0
        # edge cases: [["1"]] or [["0"]]

        # setup variables: numIslands = 0, visited= set() (fill with rows and cols)
        numIslands = 0
        visited = set()

        def dfs(r,c):
            if (r,c) not in visited and grid[r][c] == '1':
                visited.add((r,c))    
                # go top, down, left, right (accounting for the edges in the graph)
                up, down, left, right = (r-1,c), (r+1, c), (r,c-1), (r,c+1)

                if up[0] >= 0:
                    dfs(*up)    
                if down[0] < len(grid):
                    dfs(*down)
                if left[1] >=0:
                    dfs(*left)
                if right[1] < len(grid[0]):
                    dfs(*right)

        # loop through grid:
        # loop through row:
        for r in range(len(grid)):
            # loop through cols: 
            for c in range(len(grid[0])):
                
                # if it is not visited and the value is '1'
                if (r,c) not in visited and grid[r][c] == '1':
                    # use dfs on that value
                    dfs(r,c)
                    numIslands += 1
                
                # else
                    # go to the next iteration
        return numIslands
        # time: O(n.m)
        # space: O(n.m)

        """
        grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
(0,0) -> (0-1)
        """