from heapq import heappop, heappush

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        if n == 1:
            return 0
            
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        INF = 10**15
        dist = [INF] * (n * k)
        dist[0] = 0  # node = 0, run = 1 -> 0 * k + (1 - 1) = 0
        
        target = n - 1
        MASK = (1 << 22) - 1
        pq = [0]  # (0 << 22) | 0
        
        while pq:
            entry = heappop(pq)
            d = entry >> 22
            state = entry & MASK
            
            if d > dist[state]:
                continue
                
            u, rem = divmod(state, k)
            if u == target:
                return d
                
            run = rem + 1
            lu = labels[u]
            
            for v, w in adj[u]:
                nrun = run + 1 if labels[v] == lu else 1
                if nrun <= k:
                    nd = d + w
                    nstate = v * k + nrun - 1
                    if nd < dist[nstate]:
                        dist[nstate] = nd
                        heappush(pq, (nd << 22) | nstate)
                        
        return -1