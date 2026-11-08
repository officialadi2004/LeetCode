class Solution(object):
    def sumCounts(self, nums):
        MOD = 1000000007
        n = len(nums)
        
        # 1-indexed BIT arrays to avoid offset overhead and negative index issues
        # Size 2*n + 4 provides safety for (r + 2) updates
        tree1 = [0] * (n + 3)
        tree2 = [0] * (n + 3)
        
        def add(idx, val):
            v_mul = (idx - 1) * val
            while idx <= n + 1:
                tree1[idx] += val
                tree2[idx] += v_mul
                idx += idx & (-idx)

        def query(idx):
            s1 = 0
            s2 = 0
            cur = idx
            while cur > 0:
                s1 += tree1[cur]
                s2 += tree2[cur]
                cur -= cur & (-cur)
            return idx * s1 - s2

        last_pos = {}
        total_sq = 0
        ans = 0
        
        for i, val in enumerate(nums):
            prev = last_pos.get(val, -1)
            # Map 0-indexed bounds [prev + 1, i] to 1-indexed [l, r]
            l = prev + 2
            r = i + 1
            
            # Query sum of elements in 1-indexed range [l, r]
            sum_d = query(r) - query(l - 1)
            
            # Update running sum of squares: (d + 1)^2 - d^2 = 2*d + 1
            total_sq = (total_sq + 2 * sum_d + (r - l + 1)) % MOD
            ans = (ans + total_sq) % MOD
            
            # Range update +1 on [l, r]
            add(l, 1)
            add(r + 1, -1)
            
            last_pos[val] = i
            
        return ans