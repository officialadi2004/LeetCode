
class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1
            costs.append(cost)

        # Topological order
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        order = []
        idx = 0
        while idx < len(queue):
            u = queue[idx]
            idx += 1
            order.append(u)

            for v, cost in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        def can_reach(threshold):
            INF = 10**30
            dist = [INF] * n
            dist[0] = 0

            for u in order:
                if dist[u] == INF or not online[u]:
                    continue

                for v, cost in graph[u]:
                    if cost >= threshold and online[v]:
                        new_cost = dist[u] + cost
                        if new_cost < dist[v]:
                            dist[v] = new_cost

            return dist[n - 1] <= k

        if not edges or not can_reach(0):
            return -1

        left, right = 0, max(costs)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
