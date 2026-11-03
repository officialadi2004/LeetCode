from collections import Counter

class Solution(object):
    def totalNumbers(self, digits):
        available = Counter(digits)
        count = 0
        
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            req = Counter([d1, d2, d3])
            
            if all(available[d] >= req[d] for d in req):
                count += 1
                
        return count