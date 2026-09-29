class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        length = m + n - 1

        # Valid parentheses string must have even length
        if length % 2:
            return False

        # Starting cell must be '('
        if grid[0][0] == ')':
            return False

        dp = [set() for _ in range(n)]
        dp[0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = 1 if grid[i][j] == '(' else -1
                new = set()

                if i > 0:
                    for balance in dp[j]:
                        nb = balance + value
                        if nb >= 0:
                            new.add(nb)

                if j > 0:
                    for balance in dp[j - 1]:
                        nb = balance + value
                        if nb >= 0:
                            new.add(nb)

                dp[j] = new

        return 0 in dp[n - 1]