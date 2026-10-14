
class Solution:
    def maxBuilding(self, n, restrictions):
        r = [[1, 0]] + [x[:] for x in restrictions]
        r.sort()

        if r[-1][0] != n:
            r.append([n, n - 1])

        m = len(r)

        for i in range(1, m):
            d = r[i][0] - r[i - 1][0]
            r[i][1] = min(r[i][1], r[i - 1][1] + d)
        for i in range(m - 2, -1, -1):
            d = r[i + 1][0] - r[i][0]
            r[i][1] = min(r[i][1], r[i + 1][1] + d)
        ans = 0
        for i in range(1, m):
            x1, h1 = r[i - 1]
            x2, h2 = r[i]
            d = x2 - x1
            ans = max(ans, (h1 + h2 + d) // 2)

        return ans
