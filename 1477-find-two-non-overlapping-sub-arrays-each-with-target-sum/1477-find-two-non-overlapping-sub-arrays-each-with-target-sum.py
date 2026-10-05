class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1

        best = [INF] * n
        left = 0
        total = 0
        ans = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                best[right] = min(
                    length,
                    best[right - 1] if right > 0 else INF
                )
            else:
                best[right] = best[right - 1] if right > 0 else INF

        return -1 if ans == INF else ans