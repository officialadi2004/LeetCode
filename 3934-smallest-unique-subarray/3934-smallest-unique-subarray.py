class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        if n == 1:
            return 1

        # 1. Fast-path O(n) check for length 1 using 1-byte-per-value bytearray
        max_v = max(nums)
        seen1 = bytearray(max_v + 1)
        for x in nums:
            st = seen1[x]
            if st == 0:
                seen1[x] = 1
            elif st == 1:
                seen1[x] = 2
        for x in nums:
            if seen1[x] == 1:
                return 1
        del seen1

        # 2. Binary search on subarray length L in [2..n] using 64-bit rolling hash
        # Two coprime odd bases combined into a 128-bit key eliminates collision risk
        B1 = 1000003
        B2 = 1000033
        M64 = 0xFFFFFFFFFFFFFFFF

        def has_unique(L):
            p1 = pow(B1, L, 1 << 64)
            p2 = pow(B2, L, 1 << 64)

            h1 = 0
            h2 = 0
            for i in range(L):
                x = nums[i]
                h1 = (h1 * B1 + x) & M64
                h2 = (h2 * B2 + x) & M64

            # Map 128-bit hash -> first start index (or -1 if duplicated)
            seen = {(h1 << 64) | h2: 0}

            for i in range(L, n):
                out_v = nums[i - L]
                in_v = nums[i]
                h1 = (h1 * B1 + in_v - out_v * p1) & M64
                h2 = (h2 * B2 + in_v - out_v * p2) & M64
                key = (h1 << 64) | h2
                if key in seen:
                    seen[key] = -1
                else:
                    seen[key] = i - L + 1

            for idx in seen.values():
                if idx != -1:
                    return True
            return False

        lo = 2
        hi = n
        while lo < hi:
            mid = (lo + hi) >> 1
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo