class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        try:
            start = nums.index(target)
            return list(range(start, start + nums.count(target)))
        except ValueError:
            return []