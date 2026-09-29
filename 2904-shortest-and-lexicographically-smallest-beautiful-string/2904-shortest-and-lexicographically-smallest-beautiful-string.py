class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        left = 0
        ones = 0
        best_l = -1
        best_r = -1
        best_len = n + 1

        for right in range(n):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                while s[left] == '0':
                    left += 1

                length = right - left + 1

                if length < best_len:
                    best_len = length
                    best_l = left
                    best_r = right
                elif length == best_len:
                    if s[left:right + 1] < s[best_l:best_r + 1]:
                        best_l = left
                        best_r = right

        if best_l == -1:
            return ""

        return s[best_l:best_r + 1]