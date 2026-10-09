class Solution:
    def minInsertions(self, s):
        open_needed = 0
        ans = 0

        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open_needed += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1

                if open_needed > 0:
                    open_needed -= 1
                else:
                    ans += 1

            i += 1

        return ans + open_needed * 2