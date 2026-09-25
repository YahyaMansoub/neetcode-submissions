class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        q = deque()
        for r in range(rows):
            if board[r][0]=='O':
               q.append((r, 0))
            if board[r][cols-1]=='O':
                q.append((r, cols-1))

        for c in range(1, cols-1):
            if board[0][c]=='O':
               q.append((0, c))
            if board[rows-1][c]=='O':
                q.append((rows - 1, c))
        directions = [
    (1, 0),   # down
    (-1, 0),  # up
    (0, 1),   # right
    (0, -1)   # left
]
        visited = set(q)
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                 nr = r + dr
                 nc = c + dc
                 if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited:
                     continue 
                 if board[nr][nc]=='X':
                     continue
                 visited.add((nr, nc))
                 q.append((nr, nc))
        
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c]='X'

        
        
          

            

