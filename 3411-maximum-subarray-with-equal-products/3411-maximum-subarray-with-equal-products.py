class Solution(object):
    def maxLength(self, nums):
        # 4-bit prime factor masks for 0..10 packed into a single integer:
        # primes <= 10 are {2:1, 3:2, 5:4, 7:8}
        # index:  10    9    8    7    6    5    4    3    2    1    0
        # mask:  0101 0010 0001 1000 0011 0100 0001 0010 0001 0000 0000 = 0x52183412100
        MASKS = 0x52183412100
        
        ans = 2  # Any subarray of length 2 always satisfies prod == lcm * gcd
        window_mask = 0
        l = 0
        
        for r, x in enumerate(nums):
            m = (MASKS >> (x << 2)) & 15
            while window_mask & m:
                window_mask ^= (MASKS >> (nums[l] << 2)) & 15
                l += 1
            window_mask |= m
            if r - l + 1 > ans:
                ans = r - l + 1
                
        return ans