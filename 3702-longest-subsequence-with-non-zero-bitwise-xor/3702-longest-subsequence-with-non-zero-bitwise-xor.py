class Solution:
    def longestSubsequence(self, nums):
        total = 0
        has_nonzero = False
        n = len(nums)

        for x in nums:
            total ^= x
            if x != 0:
                has_nonzero = True

        if total != 0:
            return n

        if not has_nonzero:
            return 0

        return n - 1