
class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        for j in range(1, LOG):
            prev = parent[j - 1]
            curr = parent[j]
            for u in range(n):
                curr[u] = prev[prev[u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit_pos = 0

            while diff:
                if diff & 1:
                    u = parent[bit_pos][u]
                diff >>= 1
                bit_pos += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        # Fenwick tree using XOR
        bit = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def prefix(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        chars = [1 << (ord(c) - ord('a')) for c in s]

        for u in range(n):
            add(tin[u], chars[u])
            add(tout[u], chars[u])

        def path_mask(u, v):
            w = lca(u, v)
            return prefix(tin[u]) ^ prefix(tin[v]) ^ chars[w]

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = 1 << (ord(parts[2]) - ord('a'))

                delta = chars[u] ^ new_char
                add(tin[u], delta)
                add(tout[u], delta)
                chars[u] = new_char
            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_mask(u, v)
                ans.append((mask & (mask - 1)) == 0)

        return ans
