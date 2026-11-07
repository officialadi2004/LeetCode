class Solution(object):
    def maxProduct(self, n):
        digits = sorted([int(d) for d in str(n)], reverse=True)
        return digits[0] * digits[1]