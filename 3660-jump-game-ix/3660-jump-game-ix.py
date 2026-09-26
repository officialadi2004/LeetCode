class Solution:
    def maxValue(self, nums):
        n = len(nums)

        # Maximum value from index 0 to i
        prefix_max = [0] * n
        prefix_max[0] = nums[0]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        ans = [0] * n
        suffix_min = float('inf')

        # Process from right to left
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                ans[i] = prefix_max[i]
            elif prefix_max[i] > suffix_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = prefix_max[i]

            suffix_min = min(suffix_min, nums[i])

        return ans