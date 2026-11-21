class Solution(object):
    def maxDepthAfterSplit(self, seq):
        ans = [0] * len(seq)
        bit = 0
        for i, ch in enumerate(seq):
            if ch == '(':
                bit ^= 1
                ans[i] = bit
            else:
                ans[i] = bit
                bit ^= 1
        return ans