
class Solution:
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i]:
                continue

            stack = [i]
            visited[i] = True
            nodes = 0
            degree_sum = 0

            while stack:
                u = stack.pop()
                nodes += 1
                degree_sum += len(graph[u])

                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)

            if degree_sum == nodes * (nodes - 1):
                ans += 1

        return ans
