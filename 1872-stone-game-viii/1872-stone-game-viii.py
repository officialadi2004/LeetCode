class Solution:
    def stoneGameVIII(self, stones):
        total = 0

        for i in range(len(stones)):
            total += stones[i]
            stones[i] = total

        ans = stones[-1]

        for i in range(len(stones) - 2, 0, -1):
            x = stones[i] - ans
            if x > ans:
                ans = x

        return ans