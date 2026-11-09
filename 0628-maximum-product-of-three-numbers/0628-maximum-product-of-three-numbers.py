class Solution(object):
    def maximumProduct(self, nums):
        # 3 largest elements
        max1 = max2 = max3 = float('-inf')
        # 2 smallest elements
        min1 = min2 = float('inf')

        for x in nums:
            # Update maximums
            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x

            # Update minimums
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        prod1 = max1 * max2 * max3
        prod2 = min1 * min2 * max1

        return prod1 if prod1 > prod2 else prod2