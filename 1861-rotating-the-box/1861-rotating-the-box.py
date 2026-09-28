class Solution:
    def rotateTheBox(self, boxGrid):
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Gravity
        for i in range(m):
            empty = n - 1

            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty = j - 1

                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty] = '#'
                    empty -= 1

        # Rotate 90 degrees clockwise
        ans = []

        for j in range(n):
            row = []
            for i in range(m - 1, -1, -1):
                row.append(boxGrid[i][j])
            ans.append(row)

        return ans