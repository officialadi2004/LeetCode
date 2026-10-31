class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        # leftBest[i][j] =
        # max(dp[i][k] + sum(i..k)) for i <= k <= j
        leftBest = [[0] * n for _ in range(n)]

        # rightBest[i][j] =
        # max(dp[k][j] + sum(k..j)) for i <= k <= j
        rightBest = [[0] * n for _ in range(n)]

        for i in range(n):
            leftBest[i][i] = stoneValue[i]
            rightBest[i][i] = stoneValue[i]

        # Process from bottom to top
        for i in range(n - 2, -1, -1):
            p = i - 1

            for j in range(i + 1, n):
                total = prefix[j + 1] - prefix[i]

                # Largest split p where leftSum <= rightSum
                while p + 1 < j:
                    left = prefix[p + 2] - prefix[i]

                    if left * 2 <= total:
                        p += 1
                    else:
                        break

                best = 0

                # Splits where LEFT side is smaller
                if p >= i:
                    best = leftBest[i][p]

                # Check whether split p has equal sums
                equal = False
                if p >= i:
                    left = prefix[p + 1] - prefix[i]
                    equal = (left * 2 == total)

                if equal:
                    # For equal sums, Alice can choose either side
                    if p + 1 <= j:
                        best = max(best, rightBest[p + 1][j])
                else:
                    # For splits after p, RIGHT side is smaller
                    if p + 2 <= j:
                        best = max(best, rightBest[p + 2][j])

                dp[i][j] = best

                leftBest[i][j] = max(
                    leftBest[i][j - 1],
                    dp[i][j] + total
                )

                rightBest[i][j] = max(
                    rightBest[i + 1][j],
                    dp[i][j] + total
                )

        return dp[0][n - 1]