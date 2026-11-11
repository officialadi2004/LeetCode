class Solution(object):
    def countServers(self, n, logs, x, queries):
        # Sort logs by timestamp
        logs.sort(key=lambda item: item[1])
        
        # Sort queries while preserving original indices
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        # Frequency array for server request counts in the current window
        server_cnt = [0] * (n + 1)
        active_servers = 0
        
        ans = [0] * len(queries)
        left = 0
        right = 0
        num_logs = len(logs)
        
        for orig_idx, q_time in sorted_queries:
            win_start = q_time - x
            win_end = q_time
            
            # Expand right pointer: include all logs with timestamp <= win_end
            while right < num_logs and logs[right][1] <= win_end:
                s_id = logs[right][0]
                if server_cnt[s_id] == 0:
                    active_servers += 1
                server_cnt[s_id] += 1
                right += 1
                
            # Contract left pointer: exclude all logs with timestamp < win_start
            while left < num_logs and logs[left][1] < win_start:
                s_id = logs[left][0]
                server_cnt[s_id] -= 1
                if server_cnt[s_id] == 0:
                    active_servers -= 1
                left += 1
                
            ans[orig_idx] = n - active_servers
            
        return ans