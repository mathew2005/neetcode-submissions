class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            sumRow = 0
            for c in range(COLS):
                sumRow += matrix[r][c]
                self.sumMat[r+1][c+1] += self.sumMat[r][c+1] + sumRow
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMat[row2 + 1][col2 + 1] - self.sumMat[row1][col2 + 1] - self.sumMat[row2 + 1][col1] + self.sumMat[row1][col1]


# 1. loop through the methods and executes it
# 2. build a new matrix (numMatrix)
# 3. build a sumRegion method

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)