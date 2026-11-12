class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0
        
        d = 1
        while d * d <= n:
            if n % d == 0:
                for k in (d, n // d) if d * d != n else (d,):
                    prev_max = -1
                    valid = True
                    
                    for L in range(0, n, k):
                        R = L + k - 1
                        drop_idx = -1
                        
                        for i in range(L, R):
                            if nums[i] > nums[i + 1]:
                                if drop_idx != -1:
                                    valid = False
                                    break
                                drop_idx = i
                                
                        if not valid:
                            break
                            
                        if drop_idx == -1:
                            b_min = nums[L]
                            b_max = nums[R]
                        elif nums[R] <= nums[L]:
                            b_max = nums[drop_idx]
                            b_min = nums[drop_idx + 1]
                        else:
                            valid = False
                            break
                            
                        if prev_max > b_min:
                            valid = False
                            break
                        prev_max = b_max
                        
                    if valid:
                        ans += k
            d += 1
            
        return ans