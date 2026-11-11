class Solution(object):
    def uniqueXorTriplets(self, nums):
        unique = list(set(nums))
        
        # Max value is 1500 < 2048, so all XORs fit in 11 bits (< 2048)
        # Fast boolean lookup table for pair XORs
        has_pair = [False] * 2048
        pairs = []
        
        for i, a in enumerate(unique):
            for b in unique[i:]:
                val = a ^ b
                if not has_pair[val]:
                    has_pair[val] = True
                    pairs.append(val)
                    
        # Fast boolean lookup table for triplet XORs
        has_triplet = [False] * 2048
        ans = 0
        
        for p in pairs:
            for u in unique:
                val = p ^ u
                if not has_triplet[val]:
                    has_triplet[val] = True
                    ans += 1
                    if ans == 2048:
                        return 2048
                        
        return ans