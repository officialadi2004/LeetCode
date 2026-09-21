class Solution:
    def resultArray(self, nums, k):

        ans = [0] * k

        # dp[r] = number of subarrays ending at previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:

            x = num % k
            new_dp = [0] * k

            # Start a new subarray with just this number
            new_dp[x] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * x) % k
                    new_dp[new_r] += dp[r]

            # Add all subarrays ending here
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans