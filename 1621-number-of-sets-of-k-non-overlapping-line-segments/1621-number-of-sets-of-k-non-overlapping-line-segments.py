
class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        total = n + k - 1
        r = 2 * k

        ans = 1
        for i in range(1, r + 1):
            ans = ans * (total - r + i) % MOD
            ans = ans * pow(i, MOD - 2, MOD) % MOD

        return ans
