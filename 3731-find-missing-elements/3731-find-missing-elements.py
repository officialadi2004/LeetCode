class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        ans = []
        extend = ans.extend
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                extend(xrange(nums[i - 1] + 1, nums[i]))
        return ans