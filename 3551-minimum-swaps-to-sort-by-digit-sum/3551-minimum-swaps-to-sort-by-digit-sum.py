class Solution:
    def minSwaps(self, nums):
        n = len(nums)

        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        arr = sorted((digit_sum(x), x, i) for i, x in enumerate(nums))
        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle += 1

            ans += cycle - 1

        return ans