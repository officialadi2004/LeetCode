class Solution:
    def findSafeWalk(self, grid, health):
        m = len(grid)
        n = len(grid[0])

        best = [[0] * n for _ in range(m)]
        best[0][0] = health - grid[0][0]

        queue = [(0, 0)]
        head = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while head < len(queue):
            r, c = queue[head]
            head += 1

            current = best[r][c]

            if r == m - 1 and c == n - 1:
                return current > 0

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_health = current - grid[nr][nc]

                    if new_health > 0 and new_health > best[nr][nc]:
                        best[nr][nc] = new_health
                        queue.append((nr, nc))

        return False