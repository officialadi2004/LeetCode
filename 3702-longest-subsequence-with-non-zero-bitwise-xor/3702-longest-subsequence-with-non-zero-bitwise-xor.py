class Solution(object):
    def longestSubsequence(self, nums):
        total_xor = 0
        has_nonzero = False
        
        for x in nums:
            total_xor ^= x
            if x != 0:
                has_nonzero = True
                
        if not has_nonzero:
            return 0
            
        if total_xor != 0:
            return len(nums)
            
        return len(nums) - 1