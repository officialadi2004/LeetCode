
class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        depth = [0] * (n + 1)
        up = [[0] * (n + 1) for _ in range(LOG)]

        stack = [1]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v == up[0][u]:
                    continue
                up[0][v] = u
                depth[v] = depth[u] + 1
                stack.append(v)

        for j in range(1, LOG):
            prev = up[j - 1]
            curr = up[j]
            for v in range(1, n + 1):
                curr[v] = prev[prev[v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        ans = []
        for u, v in queries:
            w = lca(u, v)
            length = depth[u] + depth[v] - 2 * depth[w]

            if length == 0:
                ans.append(0)
            else:
                ans.append(pow(2, length - 1, MOD))

        return ans
