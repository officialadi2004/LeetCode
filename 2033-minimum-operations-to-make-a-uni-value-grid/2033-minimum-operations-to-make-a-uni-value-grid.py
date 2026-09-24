class Solution:
    def minOperations(self, grid, x):
        nums = []

        for row in grid:
            for num in row:
                nums.append(num)

        # Check if conversion is possible
        remainder = nums[0] % x

        for num in nums:
            if num % x != remainder:
                return -1

        # Median minimizes total absolute difference
        nums.sort()
        median = nums[len(nums) // 2]

        operations = 0

        for num in nums:
            operations += abs(num - median) // x

        return operations