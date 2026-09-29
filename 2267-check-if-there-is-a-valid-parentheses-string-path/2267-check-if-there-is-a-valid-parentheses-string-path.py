class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        length = m + n - 1

        if length % 2 or grid[0][0] == ')':
            return False

        # dp[j]: possible balances represented as bits
        dp = [0] * n
        dp[0] = 1 << 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                bits = 0

                if i > 0:
                    bits |= dp[j]

                if j > 0:
                    bits |= dp[j - 1]

                if grid[i][j] == '(':
                    bits <<= 1
                else:
                    bits >>= 1

                dp[j] = bits

        return (dp[n - 1] & 1) != 0