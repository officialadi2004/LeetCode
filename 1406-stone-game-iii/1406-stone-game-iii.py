
class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp1 = dp2 = dp3 = 0

        for i in range(n - 1, -1, -1):
            x = stoneValue[i]
            best = x - dp1

            if i + 1 < n:
                best = max(best, x + stoneValue[i + 1] - dp2)

            if i + 2 < n:
                best = max(
                    best,
                    x + stoneValue[i + 1] + stoneValue[i + 2] - dp3
                )

            dp3, dp2, dp1 = dp2, dp1, best

        if dp1 > 0:
            return "Alice"
        if dp1 < 0:
            return "Bob"
        return "Tie"
