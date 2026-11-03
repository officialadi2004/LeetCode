class Solution(object):
    def minMoves(self, nums):
        return len(nums) * max(nums) - sum(nums)