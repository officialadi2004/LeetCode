class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        if n <= 1:
            return 0

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        # max_l[i][j] = max_{i <= k <= j} (dp[i][k] + (pref[k+1] - pref[i]))
        max_l = [[0] * n for _ in range(n)]
        # max_r[i][j] = max_{i <= k <= j} (dp[k][j] + (pref[j+1] - pref[k]))
        max_r = [[0] * n for _ in range(n)]

        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            mid = 0
            for i in range(n - length + 1):
                j = i + length - 1
                if mid < i:
                    mid = i

                total = pref[j + 1] - pref[i]

                # Advance mid to the largest split point where left_sum <= right_sum
                while mid < j and (pref[mid + 1] - pref[i]) * 2 <= total:
                    mid += 1

                best = 0

                # 1. Splits with left_sum < right_sum: k in [i, mid - 1]
                # If left_sum == right_sum at mid - 1, handle separately
                k_limit = mid - 1
                if k_limit >= i and (pref[k_limit + 1] - pref[i]) * 2 == total:
                    # Equal sums at k_limit
                    left_res = dp[i][k_limit] + (pref[k_limit + 1] - pref[i])
                    right_res = dp[k_limit + 1][j] + (pref[j + 1] - pref[k_limit + 1])
                    cand = max(left_res, right_res)
                    if cand > best:
                        best = cand
                    k_limit -= 1

                if k_limit >= i:
                    cand = max_l[i][k_limit]
                    if cand > best:
                        best = cand

                # 2. Splits with left_sum > right_sum: k in [mid, j - 1]
                # If left_sum == right_sum at mid, handle separately
                k_start = mid
                if k_start < j and (pref[k_start + 1] - pref[i]) * 2 == total:
                    left_res = dp[i][k_start] + (pref[k_start + 1] - pref[i])
                    right_res = dp[k_start + 1][j] + (pref[j + 1] - pref[k_start + 1])
                    cand = max(left_res, right_res)
                    if cand > best:
                        best = cand
                    k_start += 1

                if k_start + 1 <= j:
                    cand = max_r[k_start + 1][j]
                    if cand > best:
                        best = cand

                dp[i][j] = best
                max_l[i][j] = max(max_l[i][j - 1], best + total)
                max_r[i][j] = max(max_r[i + 1][j], best + total)

        return dp[0][n - 1]