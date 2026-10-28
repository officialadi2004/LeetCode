
class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        arr = sorted((value, i) for i, value in enumerate(nums))
        ans = [0] * n

        i = 0

        while i < n:
            j = i + 1

            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            indices = sorted(arr[k][1] for k in range(i, j))
            values = [arr[k][0] for k in range(i, j)]

            for idx, value in zip(indices, values):
                ans[idx] = value

            i = j

        return ans
