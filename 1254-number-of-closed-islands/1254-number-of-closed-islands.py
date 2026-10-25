class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue

                stack = [(i, j)]
                grid[i][j] = 1
                closed = True

                while stack:
                    r, c = stack.pop()

                    if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                        closed = False

                    for nr, nc in ((r - 1, c), (r + 1, c),
                                   (r, c - 1), (r, c + 1)):
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            stack.append((nr, nc))

                if closed:
                    ans += 1

        return ans