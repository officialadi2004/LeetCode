class Solution:
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(set(arr))

        rank = {}
        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]

        return arr