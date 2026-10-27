
class Solution:
    def maxIceCream(self, costs, coins):
        count = [0] * 100001

        for cost in costs:
            count[cost] += 1

        bars = 0

        for cost in range(1, 100001):
            if count[cost]:
                buy = min(count[cost], coins // cost)
                bars += buy
                coins -= buy * cost

                if coins < cost:
                    break

        return bars
