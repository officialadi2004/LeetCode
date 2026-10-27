
class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        a = b = c = 0

        for i in range(n - 1, -1, -1):
            best = float('-inf')
            total = 0

            for take in range(1, min(3, n - i) + 1):
                total += stoneValue[i + take - 1]

                if take == 1:
                    next_dp = a
                elif take == 2:
                    next_dp = b
                else:
                    next_dp = c

                best = max(best, total - next_dp)

            c, b, a = b, a, best

        if a > 0:
            return "Alice"
        elif a < 0:
            return "Bob"
        return "Tie"
