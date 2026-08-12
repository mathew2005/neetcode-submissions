from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        perimeter = 0
        def bfs(r,c):
            directions = [[-1,0], [1,0], [0,1], [0,-1]]
            for dr,dc in directions:
                nr, nc = r + dr, c + dc
                nonlocal perimeter
                if (nr,nc) not in visited:
                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        perimeter += 1
                    elif grid[nr][nc] == 0:
                        perimeter += 1
                    else:
                        visited.add((nr,nc))
                        q.append((nr,nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r,c))
                    visited.add((r,c))
                    bfs(r,c)
        
        
        return perimeter
        
