class Solution:
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(coins)
        limit = min(coins) * k
        subsets = []

        for mask in range(1, 1 << n):
            value = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    g = gcd(value, coins[i])
                    value = value // g * coins[i]

                    if value > limit:
                        break

            if value <= limit:
                if bits & 1:
                    subsets.append(value)
                else:
                    subsets.append(-value)

        def count(x):
            total = 0

            for v in subsets:
                if v > 0:
                    total += x // v
                else:
                    total -= x // (-v)

            return total

        left = 1
        right = limit

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left