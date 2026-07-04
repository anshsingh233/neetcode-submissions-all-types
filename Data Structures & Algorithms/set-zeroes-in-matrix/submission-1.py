class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols=len(matrix),len(matrix[0])
        ROWS,COLS=[False]*rows,[False]*cols
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    ROWS[r]=True
                    COLS[c]=True
        for r in range(rows):
            for c in range(cols):
                if ROWS[r] or COLS[c]:
                    matrix[r][c]=0
        