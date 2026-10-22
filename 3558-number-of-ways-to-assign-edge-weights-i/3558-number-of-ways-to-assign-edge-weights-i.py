class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        stack = [(1, 0)]
        max_depth = 0

        while stack:
            u, parent = stack.pop()
            for v in graph[u]:
                if v != parent:
                    depth[v] = depth[u] + 1
                    max_depth = max(max_depth, depth[v])
                    stack.append((v, u))

        return pow(2, max_depth - 1, MOD)