class Solution:
    def uniformArray(self, nums1):
        has_even = False
        has_odd = False

        for x in nums1:
            if x % 2 == 0:
                has_even = True
            else:
                has_odd = True

        return not (has_even and has_odd) or len(nums1) >= 2