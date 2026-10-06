class Solution:
    def arrayRankTransform(self, arr):
        rank = {}
        r = 1

        for num in sorted(arr):
            if num not in rank:
                rank[num] = r
                r += 1

        return [rank[num] for num in arr]