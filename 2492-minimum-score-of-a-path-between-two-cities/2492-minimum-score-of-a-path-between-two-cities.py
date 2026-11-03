from collections import deque

class Solution(object):
    def minScore(self, n, roads):
        graph = [[] for _ in range(n + 1)]
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
            
        visited = [False] * (n + 1)
        visited[1] = True
        
        queue = deque([1])
        min_score = float('inf')
        
        while queue:
            curr = queue.popleft()
            
            for neighbor, distance in graph[curr]:
                if distance < min_score:
                    min_score = distance
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    
        return min_score