class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we have one island
        # input: grid
        # top, left -> pacific
        # bottom, right -> atlantic
        # water flow -> (up, down, left, right) to a neighboring cell (if curr neighbor >= neighboring cell)
        #           -> from edge cells to ocean
        # find cells where water can flow from the cell to both pacific and atlantic using either neighboring cells or directly to the ocean
        # order doesn't matter
        # output: 2d list

        # edge case: 1x1 grid, 
        # assumptions: mxn grid
        def dfs(r,c, ocean):



            if (r,c) not in ocean:
                ocean.add((r,c))
                up, down,left,right = (r-1,c), (r+1,c), (r,c-1), (r,c+1)

                if up[0] >= 0 and heights[r][c] <= heights[up[0]][up[1]]:
                    dfs(*up,ocean)
                if down[0] <= len(heights) - 1 and heights[r][c] <= heights[down[0]][down[1]]:
                    dfs(*down, ocean)
                if left[1] >= 0 and heights[r][c] <= heights[left[0]][left[1]]:
                    dfs(*left, ocean)
                if right[1] <= len(heights[0]) - 1 and heights[r][c] <= heights[right[0]][right[1]]:
                    dfs(*right, ocean)
                

        # get border cells of grid (top,bottom,left,right)
        top, bottom, left, right = set(), set(), set(), set()
        for col in range(len(heights[0])):
            top.add((0,col))
            bottom.add((len(heights) - 1, col))
        
        for row in range(len(heights)):
            left.add((row,0))
            right.add((row, len(heights[0]) - 1))
        
        # make pacific set and atlantic set
        pacific = set()
        atlantic = set()
        combined = []
        # iterate through borders cells of grid 
        for (r,c) in top:
            dfs(r,c, pacific)
        for (r,c) in left:
            dfs(r,c, pacific)
        for (r,c) in right:
            dfs(r,c,atlantic)
        for (r,c) in bottom:
            dfs(r,c, atlantic)
        
        
        for cell in pacific:
            if cell in atlantic:
                combined.append(cell)
        
        return combined
        # use dfs to keep iterating checking (curr >= neighbor)
            # add if true
            # if not true stop iterating in that side
            # base case: having nowhere to go (all places visited)
        
    