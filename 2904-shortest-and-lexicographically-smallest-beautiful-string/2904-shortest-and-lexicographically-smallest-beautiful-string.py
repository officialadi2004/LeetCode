class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ones = [i for i, ch in enumerate(s) if ch == '1']
        if len(ones) < k:
            return ""

        min_len = float('inf')
        ans = ""

        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start:end + 1]
            length = len(sub)

            if length < min_len:
                min_len = length
                ans = sub
            elif length == min_len and (ans == "" or sub < ans):
                ans = sub

        return ans