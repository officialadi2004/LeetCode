class Solution:
    def maximumLengthSubstring(self, s):
        count = [0] * 26
        left = 0
        ans = 0

        for right in range(len(s)):
            i = ord(s[right]) - 97
            count[i] += 1

            while count[i] > 2:
                count[ord(s[left]) - 97] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans