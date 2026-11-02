from collections import deque
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        
        # Immediate edge case: start or finish has a thief
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0
        
        # 1. Multi-source BFS for thief distances
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0
                    
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        while q:
            r, c = q.popleft()
            d = dist[r][c]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = d + 1
                    q.append((nr, nc))
                    
        # 2. Modified Dijkstra (Max-Heap)
        max_safeness = [[-1] * n for _ in range(n)]
        max_safeness[0][0] = dist[0][0]
        
        heap = [(-dist[0][0], 0, 0)]
        
        while heap:
            neg_s, r, c = heapq.heappop(heap)
            curr_s = -neg_s
            
            if r == n - 1 and c == n - 1:
                return curr_s
                
            if curr_s < max_safeness[r][c]:
                continue
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    next_s = min(curr_s, dist[nr][nc])
                    if next_s > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = next_s
                        heapq.heappush(heap, (-next_s, nr, nc))
                        
        return 0