
class Solution:
    def maxBuilding(self, n, restrictions):
        restrictions = restrictions + [[1, 0]]
        restrictions.sort()

        m = len(restrictions)

        # Propagate limits from left to right
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + dist
            )

        # Propagate limits from right to left
        for i in range(m - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + dist
            )

        ans = 0

        for i in range(1, m):
            left_id, left_h = restrictions[i - 1]
            right_id, right_h = restrictions[i]

            dist = right_id - left_id
            peak = (left_h + right_h + dist) // 2
            ans = max(ans, peak)

        last_id, last_h = restrictions[-1]
        ans = max(ans, last_h + n - last_id)

        return ans
