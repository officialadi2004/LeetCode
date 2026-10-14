
class Solution:
    def maximumLength(self, nums):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        ans = 1

        for x in freq:
            if x == 1:
                ans = max(ans, freq[x] if freq[x] % 2 else freq[x] - 1)
                continue

            length = 0
            cur = x

            while freq.get(cur, 0) >= 2:
                length += 2
                cur *= cur

            if freq.get(cur, 0) >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans
