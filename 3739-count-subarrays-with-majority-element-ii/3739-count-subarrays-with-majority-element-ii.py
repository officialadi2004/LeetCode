class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        a = [0] * (n + 1)

        for i, x in enumerate(nums):
            a[i + 1] = a[i] + (1 if x == target else -1)

        def solve(l, r):
            if r - l <= 1:
                return 0

            m = (l + r) // 2
            ans = solve(l, m) + solve(m, r)

            j = m
            for i in range(l, m):
                while j < r and a[j] <= a[i]:
                    j += 1
                ans += r - j

            a[l:r] = sorted(a[l:r])
            return ans

        return solve(0, n + 1)