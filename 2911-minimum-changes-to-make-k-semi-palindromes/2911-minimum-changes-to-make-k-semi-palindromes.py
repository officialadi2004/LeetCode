class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        
        # 1. Precompute proper divisors for each length L in [2..n]
        divs = [[] for _ in range(n + 1)]
        for d in range(1, (n >> 1) + 1):
            for L in range(d + d, n + 1, d):
                divs[L].append(d)
                
        # 2. Precompute minimum changes cost[i][j] for s[i:j] (j - i >= 2)
        INF = n + 1
        cost = [[INF] * (n + 1) for _ in range(n)]
        
        for i in range(n - 1):
            row = cost[i]
            for j in range(i + 2, n + 1):
                L = j - i
                best = L >> 1  # Upper bound: d = 1 requires at most L // 2 changes
                for d in divs[L]:
                    changes = 0
                    half = (L // d) >> 1
                    span = (L // d - 1) * d
                    for r in range(d):
                        lo = i + r
                        hi = lo + span
                        for _ in range(half):
                            if s[lo] != s[hi]:
                                changes += 1
                            lo += d
                            hi -= d
                        if changes >= best:
                            break
                    if changes < best:
                        best = changes
                        if best == 0:
                            break
                row[j] = best
                
        # 3. Rolling 1D DP for k partitions (each piece has length >= 2)
        prev = cost[0][:]
        for p in range(2, k + 1):
            curr = [INF] * (n + 1)
            min_j = p << 1
            max_j = n - ((k - p) << 1)
            for j in range(min_j, max_j + 1):
                best = INF
                for i in range((p - 1) << 1, j - 1):
                    v = prev[i] + cost[i][j]
                    if v < best:
                        best = v
                curr[j] = best
            prev = curr
            
        return prev[n]