
class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        M = max(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [row[:] for row in dp]

            for a in range(M + 1):
                for b in range(M + 1):
                    ways = dp[a][b]
                    if ways == 0:
                        continue

                    g1 = gcd(a, x)
                    g2 = gcd(b, x)

                    ndp[g1][b] = (ndp[g1][b] + ways) % MOD
                    ndp[a][g2] = (ndp[a][g2] + ways) % MOD

            dp = ndp

        ans = 0
        for g in range(1, M + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans
