class Solution:
    def findMissingElements(self, nums):
        seen = set(nums)
        return [x for x in range(min(nums), max(nums) + 1) if x not in seen]