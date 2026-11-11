class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        if costBoth >= cost1 + cost2:
            return need1 * cost1 + need2 * cost2

        common = need1 if need1 < need2 else need2
        ans = common * costBoth

        rem1 = need1 - common
        rem2 = need2 - common

        if rem1 > 0:
            ans += rem1 * (cost1 if cost1 < costBoth else costBoth)
        elif rem2 > 0:
            ans += rem2 * (cost2 if cost2 < costBoth else costBoth)

        return ans