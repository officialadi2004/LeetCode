class Solution(object):
    def minScore(self, n, roads):
        parent = list(range(n + 1))
        
        def find(i):
            path = []
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for node in path:
                parent[node] = i
            return i

        for u, v, _ in roads:
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_u] = root_v

        target_root = find(1)
        min_dist = float('inf')

        for u, v, d in roads:
            if find(u) == target_root and d < min_dist:
                min_dist = d

        return min_dist