from heapq import heappop, heappush

class Solution(object):
    def busiestServers(self, k, arrival, load):
        # Free servers ordered cyclically from current request index i
        avail = list(xrange(k))
        # Busy servers bit-packed as (end_time << 17) | server_id
        busy = []
        count = [0] * k
        
        MASK = (1 << 17) - 1
        
        for i, (start, duration) in enumerate(zip(arrival, load)):
            # Release all servers finished at or before 'start'
            while busy and (busy[0] >> 17) <= start:
                s = heappop(busy) & MASK
                # Map s to its cyclic position >= i
                heappush(avail, i + ((s - i) % k))
                
            if avail:
                s = heappop(avail) % k
                count[s] += 1
                heappush(busy, ((start + duration) << 17) | s)
                
        max_req = max(count)
        return [s for s, c in enumerate(count) if c == max_req]