from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # input: mxn matrix
        # 1. set for regions to be changed
        # 2. set for regions to not be changed (do we neeed to even store this?)
        # 3. loop through set for regions to be changed from 0 to X

        # edge case: 1x1, 4x4, no O, no X,
        rows = len(board)
        cols = len(board[0])
        outergrid = deque()
        notsurrounded = set()

        # add outergrid columns
        for c in range(cols):
            if board[0][c] == 'O':
                outergrid.append((0, c))
            if board[rows - 1][c] == 'O':
                outergrid.append((rows-1, c))
        
        # add outergrid rows
        for r in range(rows):
            if board[r][0] == 'O':
                outergrid.append((r, 0))
            
            if board[r][cols-1] == 'O':
                outergrid.append((r, cols-1))
        
        # keep track of rows and cols not to change to X
        while outergrid:
            r,c = outergrid.popleft()

            if board[r][c] == 'O' and (r,c) not in notsurrounded:
                
                notsurrounded.add((r,c))

                directions = [[-1,0], [1,0], [0,-1], [0,1]]
                
                for dr,dc in directions:

                    dr = dr + r
                    dc = dc + c

                    if dr > 0 and dr < rows and dc > 0 and dc < cols and (dr,dc) not in notsurrounded and board[dr][dc] == 'O':
                        outergrid.append((dr,dc))
        
        
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == 'O' and (r,c) not in notsurrounded:
                    board[r][c] = 'X'
                    
                    
        
        