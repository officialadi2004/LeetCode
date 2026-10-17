class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        offset = n + 2
        bit = [0] * (2 * n + 5)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        prefix = 0
        ans = 0
        update(offset)

        for x in nums:
            prefix += 1 if x == target else -1
            idx = prefix + offset
            ans += query(idx - 1)
            update(idx)

        return ans