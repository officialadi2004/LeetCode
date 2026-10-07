class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        # log table
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        # Sparse tables for max and min
        levels = lg[n] + 1
        mx = [nums[:]]
        mn = [nums[:]]

        for j in range(1, levels):
            length = 1 << j
            half = length >> 1
            size = n - length + 1

            prev_max = mx[-1]
            prev_min = mn[-1]

            cur_max = [0] * size
            cur_min = [0] * size

            for i in range(size):
                cur_max[i] = max(prev_max[i], prev_max[i + half])
                cur_min[i] = min(prev_min[i], prev_min[i + half])

            mx.append(cur_max)
            mn.append(cur_min)

        def value(l, r):
            j = lg[r - l + 1]
            length = 1 << j

            maximum = max(mx[j][l], mx[j][r - length + 1])
            minimum = min(mn[j][l], mn[j][r - length + 1])

            return maximum - minimum

        import heapq

        heap = []

        # Start with [l, n-1] for every l
        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            ans -= neg_v

            if r > l:
                nr = r - 1
                v = value(l, nr)
                heapq.heappush(heap, (-v, l, nr))

        return ans