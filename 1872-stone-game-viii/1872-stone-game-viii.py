class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        total = stones[0]
        prefix = [0] * n
        prefix[0] = total

        for i in range(1, n):
            total += stones[i]
            prefix[i] = total

        ans = prefix[-1]

        for i in range(n - 2, 0, -1):
            value = prefix[i] - ans
            if value > ans:
                ans = value

        return ans