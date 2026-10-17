class Solution:
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        dp = [False] * n
        dp[0] = True
        reachable = 0

        for i in range(minJump, n):
            if dp[i - minJump]:
                reachable += 1

            if i > maxJump and dp[i - maxJump - 1]:
                reachable -= 1

            if s[i] == '0' and reachable > 0:
                dp[i] = True

        return dp[n - 1]