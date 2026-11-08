class Solution(object):
    def createGrid(self, m, n):
        # A simple canonical unique path:
        # Move all the way right along row 0: (0, 0) -> (0, n - 1)
        # Then move all the way down along col n - 1: (0, n - 1) -> (m - 1, n - 1)
        grid = [['#' for _ in range(n)] for _ in range(m)]
        
        # Free up row 0
        for c in range(n):
            grid[0][c] = '.'
            
        # Free up column n - 1
        for r in range(m):
            grid[r][n - 1] = '.'
            
        return ["".join(row) for row in grid]