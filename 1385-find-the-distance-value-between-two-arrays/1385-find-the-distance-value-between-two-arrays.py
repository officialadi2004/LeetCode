from bisect import bisect_left

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        m = len(arr2)
        
        for val in arr1:
            idx = bisect_left(arr2, val)
            valid = True
            
            if idx < m and abs(arr2[idx] - val) <= d:
                valid = False
            elif idx > 0 and abs(arr2[idx - 1] - val) <= d:
                valid = False
                
            if valid:
                count += 1
                
        return count