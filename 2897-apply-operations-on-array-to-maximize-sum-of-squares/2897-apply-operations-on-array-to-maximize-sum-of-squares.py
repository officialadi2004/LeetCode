
class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bits = [0] * 32

        for x in nums:
            b = 0
            while x:
                if x & 1:
                    bits[b] += 1
                x >>= 1
                b += 1

        ans = 0

        for _ in range(k):
            x = 0
            for b in range(32):
                if bits[b] > 0:
                    x |= 1 << b
                    bits[b] -= 1

            ans = (ans + x * x) % MOD

        return ans
