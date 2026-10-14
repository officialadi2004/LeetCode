
class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n - 1][n - 1] = (0, 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue

                best = -1
                ways = 0

                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni < n and nj < n:
                        s, w = dp[ni][nj]
                        if s > best:
                            best = s
                            ways = w
                        elif s == best and s != -1:
                            ways = (ways + w) % MOD

                if best != -1:
                    value = 0 if board[i][j] == 'E' else int(board[i][j])
                    dp[i][j] = (best + value, ways)

        score, ways = dp[0][0]
        return [score, ways] if score != -1 else [0, 0]
