from bisect import bisect_left, bisect_right

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        total_ones = s.count('1')
        
        # Segment Tree to store and query max adjacent pair sums
        # without storing large 2D sparse table matrices
        starts = []
        ends = []
        lens = []
        
        i = 0
        while i < n:
            if s[i] == '0':
                st = i
                while i < n and s[i] == '0':
                    i += 1
                starts.append(st)
                ends.append(i - 1)
                lens.append(i - st)
            else:
                i += 1
                
        m = len(lens)
        if m < 2:
            return [total_ones] * len(queries)
            
        k = m - 1
        tree = [0] * (2 * k)
        for idx in range(k):
            tree[k + idx] = lens[idx] + lens[idx + 1]
        for idx in range(k - 1, 0, -1):
            left_v = tree[idx << 1]
            right_v = tree[(idx << 1) | 1]
            tree[idx] = left_v if left_v > right_v else right_v

        def query_tree(l_idx, r_idx):
            if l_idx > r_idx:
                return 0
            l_idx += k
            r_idx += k + 1
            res = 0
            while l_idx < r_idx:
                if l_idx & 1:
                    if tree[l_idx] > res:
                        res = tree[l_idx]
                    l_idx += 1
                if r_idx & 1:
                    r_idx -= 1
                    if tree[r_idx] > res:
                        res = tree[r_idx]
                l_idx >>= 1
                r_idx >>= 1
            return res

        ans = [0] * len(queries)
        for q_idx, (l, r) in enumerate(queries):
            low = bisect_left(ends, l)
            high = bisect_right(starts, r) - 1
            
            if low >= high:
                ans[q_idx] = total_ones
                continue
                
            first_len = ends[low] - (starts[low] if starts[low] > l else l) + 1
            last_len = (ends[high] if ends[high] < r else r) - starts[high] + 1
            
            if high - low == 1:
                ans[q_idx] = total_ones + first_len + last_len
            else:
                p1 = first_len + lens[low + 1]
                p2 = lens[high - 1] + last_len
                mid_max = query_tree(low + 1, high - 2)
                best = p1 if p1 > p2 else p2
                if mid_max > best:
                    best = mid_max
                ans[q_idx] = total_ones + best
                
        return ans