class Solution:
    def minElement(self, nums):
        ans = 10**9

        for num in nums:
            total = 0

            while num:
                total += num % 10
                num //= 10

            ans = min(ans, total)

        return ans