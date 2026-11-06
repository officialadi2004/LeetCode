from bisect import bisect_left

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        m = len(arr2)
        count = 0
        
        for x in arr1:
            idx = bisect_left(arr2, x)
            if idx < m and arr2[idx] - x <= d:
                continue
            if idx > 0 and x - arr2[idx - 1] <= d:
                continue
            count += 1
            
        return count