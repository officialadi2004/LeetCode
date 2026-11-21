class Solution(object):
    def remainingMethods(self, n, k, invocations):
        m = len(invocations)
        head = [-1] * n
        to = [0] * m
        nxt = [-1] * m
        
        for idx, (u, v) in enumerate(invocations):
            to[idx] = v
            nxt[idx] = head[u]
            head[u] = idx
            
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
                
        
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(xrange(n))
                
        return [i for i in xrange(n) if not suspicious[i]]