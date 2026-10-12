
class Solution:
    def maxTotalValue(self, nums, k):
        return (max(nums) - min(nums)) * k
