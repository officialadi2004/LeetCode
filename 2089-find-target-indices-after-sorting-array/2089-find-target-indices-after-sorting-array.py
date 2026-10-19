class Solution:
    def targetIndices(self, nums, target):
        start = sum(x < target for x in nums)
        count = sum(x == target for x in nums)
        return list(range(start, start + count))