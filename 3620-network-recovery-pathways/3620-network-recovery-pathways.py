
class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        for u, v, w in edges:
            if online[u] and online[v]:
                graph[u].append((v, w))
                indegree[v] += 1
                costs.append(w)

        if not costs:
            return -1

        # Topological sorting
        queue = []
        for i in range(n):
            if online[i] and indegree[i] == 0:
                queue.append(i)

        order = []
        head = 0

        while head < len(queue):
            u = queue[head]
            head += 1
            order.append(u)

            for v, w in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        costs = sorted(set(costs))
        INF = 10**30

        def can_reach(threshold):
            dist = [INF] * n
            dist[0] = 0

            for u in order:
                d = dist[u]
                if d == INF or d > k:
                    continue

                for v, w in graph[u]:
                    if w >= threshold:
                        nd = d + w
                        if nd < dist[v]:
                            dist[v] = nd

            return dist[n - 1] <= k

        left = 0
        right = len(costs) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can_reach(costs[mid]):
                ans = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans
