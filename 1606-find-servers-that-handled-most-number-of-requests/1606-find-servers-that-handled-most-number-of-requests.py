from heapq import heappop, heappush

class Solution(object):
    def busiestServers(self, k, arrival, load):
        n = len(arrival)
        if k >= n:
            return list(xrange(n))
            
        avail = list(xrange(k))
        busy = []
        count = [0] * k
        
        for i in xrange(n):
            start = arrival[i]
            while busy and busy[0][0] <= start:
                _, s = heappop(busy)
                heappush(avail, i + ((s - i) % k))
                
            if avail:
                s = heappop(avail) % k
                count[s] += 1
                heappush(busy, (start + load[i], s))
                
        del avail, busy
        max_req = max(count)
        return [s for s in xrange(k) if count[s] == max_req]