class Solution(object):
    def remainingMethods(self, n, k, invocations):
        # 1. Flat linked-list graph (avoids allocating n separate adjacency lists)
        m = len(invocations)
        head = [-1] * n
        to = [0] * m
        nxt = [-1] * m
        
        for idx, (u, v) in enumerate(invocations):
            to[idx] = v
            nxt[idx] = head[u]
            head[u] = idx
            
        # 2. Iterative DFS from k using 1-byte-per-node bytearray
        suspicious = bytearray(n)
        suspicious[k] = 1
        stack = [k]
        
        while stack:
            u = stack.pop()
            e = head[u]
            while e != -1:
                v = to[e]
                if not suspicious[v]:
                    suspicious[v] = 1
                    stack.append(v)
                e = nxt[e]
                
        # 3. Check for any incoming edge from a non-suspicious node into a suspicious node
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(xrange(n))
                
        return [i for i in xrange(n) if not suspicious[i]]