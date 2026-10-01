class Solution:
    def minimumCost(self, cost):
        cost.sort(reverse=True)

        total = sum(cost)
        free = sum(cost[2::3])

        return total - free