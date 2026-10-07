class Solution:
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(coins)
        subsets = []

        for mask in range(1, 1 << n):
            value = 1
            bits = 0
            valid = True

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    value = value // gcd(value, coins[i]) * coins[i]

                    if value > min(coins) * k:
                        valid = False
                        break

            if valid:
                subsets.append((value, bits))

        def count(x):
            total = 0

            for value, bits in subsets:
                if value > x:
                    continue

                if bits % 2:
                    total += x // value
                else:
                    total -= x // value

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left