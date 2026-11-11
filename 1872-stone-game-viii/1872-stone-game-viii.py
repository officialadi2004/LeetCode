class Solution(object):
    def stoneGameVIII(self, stones):
        n = len(stones)
        
        # In-place prefix sum calculation to save O(n) auxiliary memory
        for i in range(1, n):
            stones[i] += stones[i - 1]
            
        # Base case: at index n - 1, the only choice is to take all stones
        best = stones[-1]
        
        # Traverse backwards from n - 2 down to 1
        for i in range(n - 2, 0, -1):
            val = stones[i] - best
            if val > best:
                best = val
                
        return best