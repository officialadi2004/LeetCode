
class Solution:
    def maxAlternatingSum(self, nums):
        nums.sort(key=abs)
        n = len(nums)
        ans = 0
        split = n // 2

        for i, x in enumerate(nums):
            if i < split:
                ans -= x * x
            else:
                ans += x * x

        return ans
