class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # down[j] = ways entering current cell from above
        down = [0] * n

        for i in range(m):
            right = 0  # ways entering current cell from the left

            for j in range(n):
                # Starting cell
                if i == 0 and j == 0:
                    ways = 1
                else:
                    ways = (right + down[j]) % MOD

                # Destination
                if i == m - 1 and j == n - 1:
                    return ways

                if grid[i][j] == 0:
                    # Normal cell: can choose Right or Down
                    right = ways
                    down[j] = ways

                else:
                    # Mirror:
                    # Entering from LEFT (moving right) → turns DOWN
                    # Entering from ABOVE (moving down) → turns RIGHT
                    old_right = right
                    old_down = down[j]

                    right = old_down % MOD
                    down[j] = old_right % MOD

        return 0