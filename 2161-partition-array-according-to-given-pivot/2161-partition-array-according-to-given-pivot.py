class Solution:
    def pivotArray(self, nums, pivot):
        left = []
        right = []
        equal = []

        for x in nums:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                equal.append(x)

        left.extend(equal)
        left.extend(right)

        return left