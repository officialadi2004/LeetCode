class Solution(object):
    def resultArray(self, nums, k):
        ans = [0] * k
        curr_dp = [0] * k
        
        for val in nums:
            rem = val % k
            next_dp = [0] * k
            # Single-element subarray starting and ending at current index
            next_dp[rem] = 1
            
            # Extend previous subarrays
            for r in range(k):
                cnt = curr_dp[r]
                if cnt:
                    next_dp[(r * rem) % k] += cnt
                    
            for r in range(k):
                ans[r] += next_dp[r]
                
            curr_dp = next_dp
            
        return ans