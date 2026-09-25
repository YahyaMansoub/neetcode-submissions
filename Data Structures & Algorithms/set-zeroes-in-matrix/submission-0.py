class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col =set(), set()
        rows , cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                
                 
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)

        
        for r in row:
            for j in range(cols):
                matrix[r][j]=0

        for c in col:
            for i in range(rows):
                matrix[i][c]=0

                   