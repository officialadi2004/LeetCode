class Solution:
    def distinctSubseqII(self, s):
        MOD = 1000000007

        dp = [0] * 26
        total = 0

        for ch in s:
            i = ord(ch) - 97

            new = (total + 1) % MOD

            total = (total + new - dp[i]) % MOD
            dp[i] = new

        return total