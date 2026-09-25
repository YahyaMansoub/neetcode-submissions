class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def bt(i,j,idx):
            
            if idx == len(word):
                return True 

            if (i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or board[i][j]!= word[idx]):
                return False

            visited[i][j] = True 

            found = (bt(i+1, j, idx+1) or  
                     bt(i-1, j, idx+1) or  
                     bt(i, j+1, idx+1) or  
                     bt(i, j-1, idx+1))   

            visited[i][j] = False

            return found 

        for r in range(rows):
            for c in range(cols):
                if bt(r, c, 0):
                    return True

        return False

            
            












        