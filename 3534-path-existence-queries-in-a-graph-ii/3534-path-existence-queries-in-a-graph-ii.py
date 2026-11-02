from bisect import bisect_right

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        vals = sorted(list(set(nums)))
        m = len(vals)
        
        comp_id = [0] * m
        curr_comp = 0
        for i in range(1, m):
            if vals[i] - vals[i - 1] > maxDiff:
                curr_comp += 1
            comp_id[i] = curr_comp
            
        LOG = 18
        jump = [[0] * m for _ in range(LOG)]
        
        for i in range(m):
            target = vals[i] + maxDiff
            idx = bisect_right(vals, target) - 1
            jump[0][i] = idx
            
        for k in range(1, LOG):
            for i in range(m):
                jump[k][i] = jump[k - 1][jump[k - 1][i]]
                
        def get_val_idx(v):
            return bisect_right(vals, v) - 1

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            val_u, val_v = nums[u], nums[v]
            
            if abs(val_u - val_v) <= maxDiff:
                ans.append(1)
                continue
                
            idx_u = get_val_idx(val_u)
            idx_v = get_val_idx(val_v)
            
            if comp_id[idx_u] != comp_id[idx_v]:
                ans.append(-1)
                continue
                
            if idx_u > idx_v:
                idx_u, idx_v = idx_v, idx_u
                
            steps = 0
            curr = idx_u
            for k in range(LOG - 1, -1, -1):
                if jump[k][curr] < idx_v:
                    curr = jump[k][curr]
                    steps += (1 << k)
                    
            ans.append(steps + 1)
            
        return ans