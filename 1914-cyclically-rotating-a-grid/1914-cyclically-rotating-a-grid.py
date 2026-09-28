class Solution:
    def rotateGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):
            top = layer
            bottom = m - 1 - layer
            left = layer
            right = n - 1 - layer

            # Extract layer in clockwise order
            arr = []

            for j in range(left, right + 1):
                arr.append(grid[top][j])

            for i in range(top + 1, bottom):
                arr.append(grid[i][right])

            for j in range(right, left - 1, -1):
                arr.append(grid[bottom][j])

            for i in range(bottom - 1, top, -1):
                arr.append(grid[i][left])

            length = len(arr)
            k2 = k % length

            # Counter-clockwise rotation
            arr = arr[k2:] + arr[:k2]

            # Put back
            idx = 0

            for j in range(left, right + 1):
                grid[top][j] = arr[idx]
                idx += 1

            for i in range(top + 1, bottom):
                grid[i][right] = arr[idx]
                idx += 1

            for j in range(right, left - 1, -1):
                grid[bottom][j] = arr[idx]
                idx += 1

            for i in range(bottom - 1, top, -1):
                grid[i][left] = arr[idx]
                idx += 1

        return grid