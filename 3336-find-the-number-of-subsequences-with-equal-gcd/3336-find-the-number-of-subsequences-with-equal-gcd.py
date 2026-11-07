from collections import defaultdict

class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        
        # Precompute GCDs for all pairs up to max(nums)
        max_val = max(nums)
        gcd_table = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        for i in range(max_val + 1):
            for j in range(max_val + 1):
                gcd_table[i][j] = gcd(i, j)

        # dp[(g1, g2)] = number of ways to have gcd of seq1 = g1, seq2 = g2
        # g1 = 0 denotes seq1 is empty, g2 = 0 denotes seq2 is empty
        dp = defaultdict(int)
        dp[(0, 0)] = 1
        
        for x in nums:
            next_dp = defaultdict(int)
            for (g1, g2), cnt in dp.items():
                # 1. Do not include x
                next_dp[(g1, g2)] = (next_dp[(g1, g2)] + cnt) % MOD
                
                # 2. Include x in seq1
                new_g1 = gcd_table[g1][x]
                next_dp[(new_g1, g2)] = (next_dp[(new_g1, g2)] + cnt) % MOD
                
                # 3. Include x in seq2
                new_g2 = gcd_table[g2][x]
                next_dp[(g1, new_g2)] = (next_dp[(g1, new_g2)] + cnt) % MOD
                
            dp = next_dp
            
        ans = 0
        for (g1, g2), cnt in dp.items():
            if g1 > 0 and g1 == g2:
                ans = (ans + cnt) % MOD
                
        return ans