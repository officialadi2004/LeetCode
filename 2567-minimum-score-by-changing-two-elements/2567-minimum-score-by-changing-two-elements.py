from heapq import nlargest, nsmallest

class Solution(object):
    def minimizeSum(self, nums):
        if len(nums) == 3:
            return 0
            
        lo = nsmallest(3, nums)
        hi = nlargest(3, nums)
        
        return min(
            hi[0] - lo[2],  # drop 2 smallest
            hi[1] - lo[1],  # drop 1 smallest, 1 largest
            hi[2] - lo[0],  # drop 2 largest
        )