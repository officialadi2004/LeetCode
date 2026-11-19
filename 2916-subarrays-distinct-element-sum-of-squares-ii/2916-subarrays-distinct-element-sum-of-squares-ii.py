class Solution(object):
    def sumCounts(self, nums):
        MOD = 1000000007
        n = len(nums)
        
        # Dual BIT for O(log n) range-add (+1) and range-sum over 1..n
        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)
        
        last_pos = [0] * (max(nums) + 1)  # 1-indexed last occurrence (0 = unseen)
        
        ans = 0
        cur_sq_sum = 0
        
        for r1, x in enumerate(nums, 1):
            l1 = last_pos[x] + 1  # 1-indexed start of range [l1, r1]
            last_pos[x] = r1
            
            # 1. Query range sum over [l1, r1] before incrementing:
            # prefix_sum(r1) - prefix_sum(l1 - 1)
            s1 = 0
            s2 = 0
            i = r1
            while i:
                s1 += bit1[i]
                s2 += bit2[i]
                i &= i - 1
            range_sum = r1 * s1 - s2
            
            l0 = l1 - 1
            if l0:
                s1 = 0
                s2 = 0
                i = l0
                while i:
                    s1 += bit1[i]
                    s2 += bit2[i]
                    i &= i - 1
                range_sum -= l0 * s1 - s2
                
            # 2. Update sum of squares: sum((c + 1)^2 - c^2) = 2 * sum(c) + length
            cur_sq_sum = (cur_sq_sum + 2 * range_sum + (r1 - l0)) % MOD
            ans += cur_sq_sum
            
            # 3. Range add +1 on [l1, r1]
            i = l1
            while i <= n:
                bit1[i] += 1
                bit2[i] += l0
                i += i & -i
                
            i = r1 + 1
            while i <= n:
                bit1[i] -= 1
                bit2[i] -= r1
                i += i & -i
                
        return ans % MOD