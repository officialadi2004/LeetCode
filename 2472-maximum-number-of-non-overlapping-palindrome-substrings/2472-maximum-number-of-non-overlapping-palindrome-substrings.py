class Solution:
    def maxPalindromes(self, s, k):

        n = len(s)

        # dp[i] = maximum number of palindromes
        # using first i characters
        dp = [0] * (n + 1)

        # Palindromes ending at previous position
        prev = bytearray(n)

        for right in range(n):

            current = bytearray(n)

            for left in range(right, -1, -1):

                # Check palindrome
                if s[left] == s[right]:

                    if right - left <= 1:
                        current[left] = 1

                    elif prev[left + 1]:
                        current[left] = 1

                # Use this palindrome if its length is >= k
                if current[left] and right - left + 1 >= k:
                    dp[right + 1] = max(
                        dp[right + 1],
                        dp[left] + 1
                    )

            # We can skip s[right]
            dp[right + 1] = max(dp[right + 1], dp[right])

            prev = current

        return dp[n]