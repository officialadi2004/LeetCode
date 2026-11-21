class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        
        # 1. Flat linked-list representation of children (zero list-of-lists overhead)
        head = [-1] * n
        nxt = [-1] * n
        for i in xrange(1, n):
            p = parent[i]
            nxt[i] = head[p]
            head[p] = i
            
        # Pre-map characters to 0..25 integers
        chars = [ord(c) - 97 for c in s]
        
        # 2. Iterative DFS to compute new parents & post-order traversal
        last = [-1] * 26
        saved = [-1] * n
        order = []
        append = order.append
        
        stack = [0]
        while stack:
            u = stack.pop()
            if u >= 0:
                c = chars[u]
                prev = last[c]
                saved[u] = prev
                if prev != -1:
                    parent[u] = prev
                last[c] = u
                stack.append(~u)
                v = head[u]
                while v != -1:
                    stack.append(v)
                    v = nxt[v]
            else:
                u = ~u
                last[chars[u]] = saved[u]
                if u:
                    append(u)
                    
        # 3. Bottom-up subtree size accumulation along post-order
        size = [1] * n
        for u in order:
            size[parent[u]] += size[u]
            
        return size