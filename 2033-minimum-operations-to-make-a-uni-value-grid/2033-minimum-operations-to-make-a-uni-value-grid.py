class Solution:
    def minOperations(self, grid, x):
        nums = [num for row in grid for num in row]

        rem = nums[0] % x

        for num in nums:
            if num % x != rem:
                return -1

        nums.sort()
        median = nums[len(nums) // 2]

        ans = 0

        for num in nums:
            ans += abs(num - median) // x

        return ans