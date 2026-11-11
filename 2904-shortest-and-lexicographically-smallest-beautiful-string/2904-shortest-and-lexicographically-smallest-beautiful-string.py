class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        if len(ones) < k:
            return ""
            
        best = None
        min_len = float('inf')
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            cur_len = end - start + 1
            
            sub = s[start:end + 1]
            if cur_len < min_len:
                min_len = cur_len
                best = sub
            elif cur_len == min_len:
                if sub < best:
                    best = sub
                    
        return best if best is not None else ""