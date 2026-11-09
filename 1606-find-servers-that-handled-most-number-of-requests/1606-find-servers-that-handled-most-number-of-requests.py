import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        # busy heap: (release_time, server_id)
        busy = []
        
        # Binary Indexed Tree (BIT) to find the next available server in O(log k)
        tree = [0] * (k + 1)
        
        def add(idx, val):
            idx += 1
            while idx <= k:
                tree[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            idx += 1
            while idx > 0:
                s += tree[idx]
                idx -= idx & (-idx)
            return s
            
        def find_kth(target):
            # Find the smallest index with prefix sum >= target
            idx = 0
            step = 1 << (k.bit_length())
            while step > 0:
                nxt = idx + step
                if nxt <= k and tree[nxt] < target:
                    idx = nxt
                    target -= tree[nxt]
                step >>= 1
            return idx  # 0-indexed server

        # Initially, all servers 0..k-1 are available
        for i in range(k):
            add(i, 1)
            
        requests_handled = [0] * k
        
        for i, (t_arr, t_load) in enumerate(zip(arrival, load)):
            # Release all finished servers
            while busy and busy[0][0] <= t_arr:
                _, s_id = heapq.heappop(busy)
                add(s_id, 1)
                
            total_free = query(k - 1)
            if total_free == 0:
                # All servers are busy, drop request
                continue
                
            target_start = i % k
            # Count free servers before target_start
            free_before = query(target_start - 1) if target_start > 0 else 0
            
            if free_before < total_free:
                # There is at least one free server in [target_start, k - 1]
                chosen_server = find_kth(free_before + 1)
            else:
                # Wrap around: pick the first available server from index 0
                chosen_server = find_kth(1)
                
            # Assign task to chosen_server
            add(chosen_server, -1)
            requests_handled[chosen_server] += 1
            heapq.heappush(busy, (t_arr + t_load, chosen_server))
            
        max_handled = max(requests_handled)
        return [idx for idx, cnt in enumerate(requests_handled) if cnt == max_handled]