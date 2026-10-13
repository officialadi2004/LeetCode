
class Solution:
    def maxAlternatingSum(self, nums):
        nums.sort(key=lambda x: x * x)
        n = len(nums)
        split = n // 2

        ans = 0
        for i in range(split):
            x = nums[i]
            ans -= x * x

        for i in range(split, n):
            x = nums[i]
            ans += x * x

        return ans
