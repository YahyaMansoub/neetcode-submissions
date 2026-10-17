class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        visited = set()

        def bt(r, c, curr):

            if curr == word:
                return True

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited
            ):
                return False

            if not word.startswith(curr + board[r][c]):
                return False

            visited.add((r, c))

            found = (
                bt(r + 1, c, curr + board[r][c]) or
                bt(r, c + 1, curr + board[r][c]) or
                bt(r - 1, c, curr + board[r][c]) or
                bt(r, c - 1, curr + board[r][c])
            )

            visited.remove((r, c))  

            return found

        for r in range(rows):
            for c in range(cols):
                if bt(r, c, ""):
                    return True

        return False

        

            
            












        