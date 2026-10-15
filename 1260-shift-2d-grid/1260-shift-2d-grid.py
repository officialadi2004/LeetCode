
class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        arr = sum(grid, [])
        k %= m * n

        arr = arr[-k:] + arr[:-k] if k else arr

        return [arr[i:i + n] for i in range(0, m * n, n)]
