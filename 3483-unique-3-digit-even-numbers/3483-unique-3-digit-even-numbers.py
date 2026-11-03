from itertools import permutations

class Solution(object):
    def totalNumbers(self, digits):
        seen = set()
        
        for d1, d2, d3 in permutations(digits, 3):
            # Must not have a leading zero, and must be even
            if d1 != 0 and d3 % 2 == 0:
                seen.add(d1 * 100 + d2 * 10 + d3)
                
        return len(seen)