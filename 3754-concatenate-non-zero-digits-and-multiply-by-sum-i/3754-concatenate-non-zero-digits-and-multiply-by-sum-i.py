
class Solution:
    def sumAndMultiply(self, n):
        x = ''.join(c for c in str(n) if c != '0')
        if not x:
            return 0

        return int(x) * sum(int(c) for c in x)
