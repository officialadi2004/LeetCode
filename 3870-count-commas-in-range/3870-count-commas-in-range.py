class Solution(object):
    def countCommas(self, n):
        return n - 999 if n >= 1000 else 0