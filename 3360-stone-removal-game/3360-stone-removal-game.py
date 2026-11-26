class Solution(object):
    def canAliceWin(self, n):
        return (10 <= n < 19) or (27 <= n < 34) or (40 <= n < 45) or (n >= 49)