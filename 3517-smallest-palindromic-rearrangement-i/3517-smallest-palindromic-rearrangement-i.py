class Solution:
    def smallestPalindrome(self, s):
        n = len(s)
        left = ''.join(sorted(s[:n // 2]))
        mid = s[n // 2] if n % 2 else ''
        return left + mid + left[::-1]