class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # dp = best score difference from this point
        dp = stones[n - 1]

        for i in range(n - 2, 0, -1):
            dp = max(dp, stones[i] - dp)

        return dp