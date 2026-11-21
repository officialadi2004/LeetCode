from collections import defaultdict

class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()
        M = nums[-1]
        
        # Use flat C-indexed list when value range is compact; O(n) dict when sparse
        if M <= 200000:
            dp = [0] * (M + 2)
            for x in nums:
                dp[x + 1] = dp[x] + 1
                dp[x] = dp[x - 1] + 1
            return max(dp)
            
        dp = defaultdict(int)
        for x in nums:
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
        return max(dp.itervalues())