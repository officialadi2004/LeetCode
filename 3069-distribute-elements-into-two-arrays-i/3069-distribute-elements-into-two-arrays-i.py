class Solution(object):
    def resultArray(self, nums):
        n = len(nums)
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        last1 = nums[0]
        last2 = nums[1]
        
        for i in range(2, n):
            x = nums[i]
            if last1 > last2:
                arr1.append(x)
                last1 = x
            else:
                arr2.append(x)
                last2 = x
                
        arr1.extend(arr2)
        return arr1