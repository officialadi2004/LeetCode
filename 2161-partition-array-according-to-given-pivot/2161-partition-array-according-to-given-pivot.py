class Solution:
    def pivotArray(self, nums, pivot):
        n = len(nums)
        ans = [0] * n
        left = 0
        equal = 0
        right = 0

        for x in nums:
            if x < pivot:
                left += 1
            elif x == pivot:
                equal += 1
            else:
                right += 1

        i = left
        j = left + equal
        l = 0

        for x in nums:
            if x < pivot:
                ans[l] = x
                l += 1
            elif x == pivot:
                ans[i] = x
                i += 1
            else:
                ans[j] = x
                j += 1

        return ans