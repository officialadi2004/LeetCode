class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        
        # 1. Collect 1-bit positions
        ones1 = []
        ones2 = []
        for r in range(n):
            for c in range(n):
                if img1[r][c]:
                    ones1.append((r, c))
                if img2[r][c]:
                    ones2.append((r, c))
        
        if not ones1 or not ones2:
            return 0
            
        # 2. Fixed-size lookup table: (2n - 1) x (2n - 1)
        stride = 2 * n
        offset = n - 1
        counts = [0] * (stride * stride)
        max_overlap = 0
        
        # 3. Direct array indexing without tuple/dict allocations
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                idx = (r2 - r1 + offset) * stride + (c2 - c1 + offset)
                counts[idx] += 1
                if counts[idx] > max_overlap:
                    max_overlap = counts[idx]
                    
        return max_overlap