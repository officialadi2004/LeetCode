import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        # busy heap: (free_time, server_id)
        busy = []
        # free heap stores virtual indices: (round_offset * k + server_id)
        # Initially, servers 0..k-1 are all available
        free = list(range(k))
        
        requests_handled = [0] * k
        
        for i, (t_arr, t_load) in enumerate(zip(arrival, load)):
            # Release all servers whose task finished by t_arr
            while busy and busy[0][0] <= t_arr:
                _, s_id = heapq.heappop(busy)
                # Map server s_id to the smallest virtual index >= i with index % k == s_id
                heapq.heappush(free, i + (s_id - i) % k)
                
            # Remove outdated virtual IDs (< i) by re-projecting them to >= i
            while free and free[0] < i:
                s_id = heapq.heappop(free) % k
                heapq.heappush(free, i + (s_id - i) % k)
                
            if not free:
                continue
                
            chosen = heapq.heappop(free) % k
            requests_handled[chosen] += 1
            heapq.heappush(busy, (t_arr + t_load, chosen))
            
        max_handled = max(requests_handled)
        return [idx for idx, cnt in enumerate(requests_handled) if cnt == max_handled]