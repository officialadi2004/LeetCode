import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        # free_servers: (weight, index)
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # busy_servers: (free_time, weight, index)
        busy_servers = []
        
        ans = [0] * len(tasks)
        time = 0
        
        for j, task_duration in enumerate(tasks):
            time = max(time, j)
            
            # If no servers are available, jump directly to the time the next server frees up
            if not free_servers and busy_servers:
                time = max(time, busy_servers[0][0])
                
            # Release all servers that are finished by the current time
            while busy_servers and busy_servers[0][0] <= time:
                free_time, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
                
            # Assign the task to the best available free server
            weight, idx = heapq.heappop(free_servers)
            ans[j] = idx
            heapq.heappush(busy_servers, (time + task_duration, weight, idx))
            
        return ans