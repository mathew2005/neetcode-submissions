class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input 9 x 9 board
            # 1. row and column must contain digits 1-9 without duplicates
            # 2. 1-9 no duplicates for the 3x3 sub-boxes
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            visited = set()
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visited: 
                    return False
                else:
                    visited.add(board[r][c])
        

        for c in range(COLS):
            visited = set()
            for r in range(ROWS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visited:
                    return False
                else:
                    visited.add(board[r][c])
        
        for r in range(0, ROWS, 3):
            for c in range(0, COLS, 3):
                visited = set()
                for nr in range(r, r + 3):
                    for nc in range(c, c + 3):
                        if board[nr][nc]  == ".":
                            continue
                        if board[nr][nc] in visited:
                            return False
                        else:
                            visited.add(board[nr][nc])


        return True
