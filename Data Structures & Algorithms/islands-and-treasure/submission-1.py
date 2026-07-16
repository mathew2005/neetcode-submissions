from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            currDistance = 0
            visited = set()
            while q:

                for _ in range(len(q)):
                    nonlocal q0
                    (r,c) = q.popleft()
                    if (r,c) not in visited and grid[r][c] != -1 and (r,c) not in q0 :
                        
                        visited.add((r,c))
                        grid[r][c] = min(grid[r][c], currDistance)
                        up, down, left, right = (r-1,c), (r+1,c), (r,c-1), (r,c+1)

                        if up[0] >= 0:
                            q.append(up)
                        if down[0] <= len(grid) - 1:
                            q.append(down)
                        if left[1] >= 0:
                            q.append(left)
                        if right[1] <= len(grid[0]) - 1:
                            q.append(right)

                    
                currDistance += 1


        q0  = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q0.add((r,c))
        

        while q0:
            curr = q0.pop()
            bfs(*curr)