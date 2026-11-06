from operator import xor

class Solution(object):
    def longestSubsequence(self, nums):
        if not any(nums):
            return 0
        return len(nums) if reduce(xor, nums) != 0 else len(nums) - 1