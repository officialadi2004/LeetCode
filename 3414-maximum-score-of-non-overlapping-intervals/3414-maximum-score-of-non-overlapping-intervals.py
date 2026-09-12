from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):

        n = len(intervals)

        # Add original index
        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append((r, l, w, i))

        # Sort by ending position
        arr.sort()

        ends = [x[0] for x in arr]

        # dp[k][i] = best answer using at most k intervals
        # from first i intervals
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):

            for i in range(1, n + 1):

                r, l, w, index = arr[i - 1]

                # Option 1: don't take this interval
                best_score, best_indices = dp[k][i - 1]

                # Find last interval whose end < current start
                j = bisect_left(ends, l, 0, i - 1)

                # Option 2: take this interval
                old_score, old_indices = dp[k - 1][j]

                new_score = old_score + w
                new_indices = tuple(sorted(old_indices + (index,)))

                # Choose better score
                if new_score > best_score:
                    dp[k][i] = (new_score, new_indices)

                # Same score -> lexicographically smaller indices
                elif new_score == best_score:
                    if new_indices < best_indices:
                        dp[k][i] = (new_score, new_indices)
                    else:
                        dp[k][i] = (best_score, best_indices)

                else:
                    dp[k][i] = (best_score, best_indices)

        return list(dp[4][n][1])