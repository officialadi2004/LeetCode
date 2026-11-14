from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        ans = 0
        cost = 0
        r = n - 1
        # Monotonic decreasing deque of indices: nums[dq[0]] > nums[dq[1]] > ...
        dq = deque()
        
        for l in range(n - 1, -1, -1):
            val = nums[l]
            # Merge segments dominated by val
            while dq and nums[dq[0]] <= val:
                idx = dq.popleft()
                nxt = dq[0] if dq else r + 1
                cost += (val - nums[idx]) * (nxt - idx)
            dq.appendleft(l)
            
            # Shrink right boundary r until cost <= k
            while cost > k:
                cost -= nums[dq[-1]] - nums[r]
                r -= 1
                if dq[-1] > r:
                    dq.pop()
                    
            ans += r - l + 1
            
        return ans