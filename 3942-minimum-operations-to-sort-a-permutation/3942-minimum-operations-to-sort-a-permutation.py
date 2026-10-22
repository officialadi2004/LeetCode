class Solution:
    def minOperations(self, nums):
        n = len(nums)

        def rotation_cost(arr):
            p = arr.index(0)

            for i in range(n):
                if arr[(p + i) % n] != i:
                    return -1

            return min(p, n - p + 2)

        ans = rotation_cost(nums)

        rev = nums[::-1]
        p = rev.index(0)

        valid = True
        for i in range(n):
            if rev[(p + i) % n] != i:
                valid = False
                break

        if valid:
            cost = 1 + min(p, n - p)
            if ans == -1 or cost < ans:
                ans = cost

        return ans