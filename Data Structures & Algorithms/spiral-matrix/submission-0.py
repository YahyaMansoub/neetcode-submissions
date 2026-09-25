class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
            
        res = []
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        
        while top <= bottom and left <= right:
            
            # 1. Traverse Right along the top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            
            # 2. Traverse Down along the right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # 3. Traverse Left along the bottom row (if row still exists)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
                
            # 4. Traverse Up along the left column (if col still exists)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
        return res