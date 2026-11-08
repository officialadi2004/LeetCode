class Solution(object):
    def createGrid(self, m, n):
        # Row 0 is entirely free: (0, 0) -> (0, n - 1)
        # All remaining rows have obstacles except the last column
        res = ["." * n]
        if m > 1:
            rest_row = "#" * (n - 1) + "."
            res.extend([rest_row] * (m - 1))
        return res