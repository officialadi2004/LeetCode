class Solution:
    def maxPalindromes(self, s, k):

        n = len(s)

        # palindrome[i][j] = True if s[i:j+1] is palindrome
        palindrome = [[False] * n for _ in range(n)]

        # Find all palindromes
        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                if s[i] == s[j]:
                    if j - i <= 2 or palindrome[i + 1][j - 1]:
                        palindrome[i][j] = True

        # dp[i] = maximum palindromes in first i characters
        dp = [0] * (n + 1)

        for end in range(n):

            # Don't use s[end] as the end of a palindrome
            dp[end + 1] = dp[end]

            # Try every possible starting position
            for start in range(end - k + 1, -1, -1):

                if palindrome[start][end]:

                    dp[end + 1] = max(
                        dp[end + 1],
                        dp[start] + 1
                    )

        return dp[n]