class Solution:
    def assignEdgeWeights(self, edges):
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [(1, 0, 0)]
        depth = 0

        while stack:
            u, parent, d = stack.pop()
            if d > depth:
                depth = d

            for v in graph[u]:
                if v != parent:
                    stack.append((v, u, d + 1))

        return pow(2, depth - 1, 1000000007)