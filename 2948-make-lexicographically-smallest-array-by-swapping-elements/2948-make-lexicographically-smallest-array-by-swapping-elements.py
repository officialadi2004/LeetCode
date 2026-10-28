
class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        arr = sorted((v, i) for i, v in enumerate(nums))
        ans = [0] * len(nums)
        n = len(nums)
        i = 0

        while i < n:
            j = i + 1

            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            indices = sorted(arr[k][1] for k in range(i, j))
            for k, idx in enumerate(indices):
                ans[idx] = arr[i + k][0]

            i = j

        return ans
