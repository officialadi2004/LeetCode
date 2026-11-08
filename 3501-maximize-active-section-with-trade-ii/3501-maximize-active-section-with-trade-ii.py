import bisect

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        total_ones = s.count('1')
        
        # Identify all contiguous blocks of '0'
        block_starts = []
        block_ends = []
        block_lens = []
        
        i = 0
        while i < n:
            if s[i] == '0':
                st = i
                while i < n and s[i] == '0':
                    i += 1
                block_starts.append(st)
                block_ends.append(i - 1)
                block_lens.append(i - st)
            else:
                i += 1
                
        m = len(block_lens)
        if m < 2:
            return [total_ones] * len(queries)
            
        # Adjacent block sums: pair_sum[i] = block_lens[i] + block_lens[i + 1]
        pair_sum = [block_lens[i] + block_lens[i + 1] for i in range(m - 1)]
        k_pairs = len(pair_sum)
        
        # Build Sparse Table for RMQ on pair_sum
        log_k = k_pairs.bit_length()
        st = [[0] * k_pairs for _ in range(log_k)]
        st[0] = list(pair_sum)
        
        for p in range(1, log_k):
            prev_row = st[p - 1]
            shift = 1 << (p - 1)
            row = st[p]
            for j in range(k_pairs - (1 << p) + 1):
                val1 = prev_row[j]
                val2 = prev_row[j + shift]
                row[j] = val1 if val1 > val2 else val2

        def query_st(l_idx, r_idx):
            if l_idx > r_idx:
                return 0
            p = (r_idx - l_idx + 1).bit_length() - 1
            return max(st[p][l_idx], st[p][r_idx - (1 << p) + 1])

        ans = []
        for l, r in queries:
            # low: index of first 0-block ending >= l
            low = bisect.bisect_left(block_ends, l)
            # high: index of last 0-block starting <= r
            high = bisect.bisect_right(block_starts, r) - 1
            
            if low >= high:
                ans.append(total_ones)
                continue
                
            first_len = block_ends[low] - max(block_starts[low], l) + 1
            last_len = min(block_ends[high], r) - block_starts[high] + 1
            
            if high - low == 1:
                ans.append(total_ones + first_len + last_len)
            else:
                pair1 = first_len + block_lens[low + 1]
                pair2 = block_lens[high - 1] + last_len
                rmq_max = query_st(low + 1, high - 2)
                max_gain = max(pair1, pair2, rmq_max)
                ans.append(total_ones + max_gain)
                
        return ans