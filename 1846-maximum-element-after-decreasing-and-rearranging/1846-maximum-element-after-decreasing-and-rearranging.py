class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()

        current = 0

        for x in arr:
            if x > current + 1:
                current += 1
            else:
                current = x

        return current