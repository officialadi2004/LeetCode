from collections import defaultdict

class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda item: item[1])
        
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda item: item[0])
        
        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        active_servers = 0
        
        left = 0
        right = 0
        m = len(logs)
        
        for q_time, orig_idx in sorted_queries:
            start_time = q_time - x
            end_time = q_time
            
            while right < m and logs[right][1] <= end_time:
                srv = logs[right][0]
                if server_counts[srv] == 0:
                    active_servers += 1
                server_counts[srv] += 1
                right += 1
                
            while left < m and logs[left][1] < start_time:
                srv = logs[left][0]
                server_counts[srv] -= 1
                if server_counts[srv] == 0:
                    active_servers -= 1
                left += 1
                
            ans[orig_idx] = n - active_servers
            
        return ans