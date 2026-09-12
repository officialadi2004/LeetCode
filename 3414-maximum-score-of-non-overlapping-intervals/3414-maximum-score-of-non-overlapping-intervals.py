from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):

        n = len(intervals)

        # (right, left, weight, original_index)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((r, l, w, i))

        arr.sort()

        ends = [x[0] for x in arr]

        # Find the last interval that ends BEFORE current interval starts
        prev = [0] * n

        for i in range(n):
            l = arr[i][1]
            prev[i] = bisect_left(ends, l, 0, i)

        # dp_score = maximum score
        # dp_indices = lexicographically smallest indices for that score
        dp_score = [0] * (n + 1)
        dp_indices = [()] * (n + 1)

        for _ in range(4):

            new_score = [0] * (n + 1)
            new_indices = [()] * (n + 1)

            for i in range(1, n + 1):

                # Don't take current interval
                score1 = new_score[i - 1]
                indices1 = new_indices[i - 1]

                r, l, w, idx = arr[i - 1]

                # Take current interval
                j = prev[i - 1]

                score2 = dp_score[j] + w

                old = dp_indices[j]
                indices2 = tuple(sorted(old + (idx,)))

                if score2 > score1:
                    new_score[i] = score2
                    new_indices[i] = indices2

                elif score2 < score1:
                    new_score[i] = score1
                    new_indices[i] = indices1

                else:
                    if indices2 < indices1:
                        new_score[i] = score2
                        new_indices[i] = indices2
                    else:
                        new_score[i] = score1
                        new_indices[i] = indices1

            dp_score = new_score
            dp_indices = new_indices

        return list(dp_indices[n])