class Solution(object):
    def targetIndices(self, nums, target):
        less = 0
        equal = 0
        for x in nums:
            less += x < target
            equal += x == target
        return [i for i in range(less, less + equal)]