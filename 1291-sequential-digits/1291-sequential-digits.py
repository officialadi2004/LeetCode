class Solution(object):
    def sequentialDigits(self, low, high):
        digits = "123456789"
        res = []
        
        for length in range(2, 10):
            for start in range(10 - length):
                val = int(digits[start : start + length])
                if low <= val <= high:
                    res.append(val)
                elif val > high:
                    return res
                    
        return res