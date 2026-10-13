
class Solution:
    def maxAlternatingSum(self, nums):
        freq = [0] * 40001

        for x in nums:
            freq[abs(x)] += 1

        n = len(nums)
        remove = n // 2
        ans = 0

        for x in range(40001):
            count = freq[x]
            take = min(count, remove)

            ans -= take * x * x
            ans += (count - take) * x * x

            remove -= take

        return ans
