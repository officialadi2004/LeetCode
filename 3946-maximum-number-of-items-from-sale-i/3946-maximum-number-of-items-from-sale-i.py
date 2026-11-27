class Solution(object):
    def maximumSaleItems(self, items, budget):
        max_f = 0
        min_p = 1501
        for f, p in items:
            if f > max_f:
                max_f = f
            if p < min_p:
                min_p = p

        # 1. Harmonic sieve in O(M log M) to count multiples of each factor
        cnt = [0] * (max_f + 1)
        for f, _ in items:
            cnt[f] += 1

        mult_cnt = [0] * (max_f + 1)
        for f in xrange(1, max_f + 1):
            if cnt[f]:
                total = 0
                for m in xrange(f, max_f + 1, f):
                    total += cnt[m]
                mult_cnt[f] = total - 1  # exclude self (j != i)

        # 2. 0/1 Knapsack for the 1st copy of each item (value = 1 + free copies)
        dp = [-1] * (budget + 1)
        dp[0] = 0
        max_c = 0

        for f, p in items:
            if p > budget:
                continue
            val = 1 + mult_cnt[f]
            new_max = max_c + p
            if new_max > budget:
                new_max = budget
            for c in xrange(new_max, p - 1, -1):
                prev = dp[c - p]
                if prev != -1 and prev + val > dp[c]:
                    dp[c] = prev + val
            if new_max > max_c:
                max_c = new_max

        # 3. Spend any remaining budget on the cheapest available item (min_p)
        ans = 0
        for c in xrange(max_c + 1):
            base = dp[c]
            if base != -1:
                total = base + (budget - c) // min_p
                if total > ans:
                    ans = total

        return ans