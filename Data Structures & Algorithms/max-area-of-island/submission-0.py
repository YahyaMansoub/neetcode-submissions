class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])


        maxArea, self.count = 0, 0
        visited = set()

        def dfs(r, c):

            if  r<0 or r >=rows or c < 0 or c >= cols:
                return 

            if (r, c) in visited or grid[r][c]==0:
                return 

            visited.add((r, c))
            self.count+=1
            dfs(r+1, c)
            dfs(r-1, c) 
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
            
                if grid[r][c]==1 and (r, c) not in visited:
                    dfs(r, c)
                    maxArea = max(maxArea, self.count)
                    self.count = 0
        return maxArea

            


