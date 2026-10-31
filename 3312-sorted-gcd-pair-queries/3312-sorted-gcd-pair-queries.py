from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        max_val = max(nums)

        # Frequency of each number
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1

        # pairs[g] = number of pairs whose gcd is exactly g
        pairs = [0] * (max_val + 1)

        # Process from larger gcd to smaller gcd
        for g in range(max_val, 0, -1):
            count = 0

            # Count numbers divisible by g
            for multiple in range(g, max_val + 1, g):
                count += freq[multiple]

            # All pairs where both numbers are divisible by g
            total = count * (count - 1) // 2

            # Remove pairs whose gcd is a multiple of g greater than g
            for multiple in range(2 * g, max_val + 1, g):
                total -= pairs[multiple]

            pairs[g] = total

        # Prefix sums: position in sorted gcdPairs
        prefix = [0] * (max_val + 1)
        running = 0

        for g in range(1, max_val + 1):
            running += pairs[g]
            prefix[g] = running

        # Find smallest gcd whose cumulative count > query
        answer = []
        for q in queries:
            answer.append(bisect_right(prefix, q))

        return answer