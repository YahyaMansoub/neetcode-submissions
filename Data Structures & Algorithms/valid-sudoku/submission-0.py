class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [set() for _ in range(9)]


        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val == ".":
                    continue
                val = int(val)
                i, j = r//3 , c//3
                coord = i*3+j
                if val in row[r] or val in col[c] or val in square[coord]:
                    
                    return False
                else:
                    row[r].add(val)
                    col[c].add(val)
                    square[coord].add(val)

        return True 