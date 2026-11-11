class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        
        # suffix_min[i] stores min(nums[i..n-1])
        suffix_min = [0] * n
        cur_min = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] < cur_min:
                cur_min = nums[i]
            suffix_min[i] = cur_min
            
        cur_max = -1
        for i in range(n):
            if nums[i] > cur_max:
                cur_max = nums[i]
            if cur_max - suffix_min[i] <= k:
                return i
                
        return -1