class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        # Offset by n so prefix sums in [-n, n] map cleanly to indices [0, 2n]
        freq = [0] * (2 * n + 2)
        
        curr = n
        freq[curr] = 1
        less_count = 0  # Number of previous prefix sums strictly less than curr
        ans = 0
        
        for x in nums:
            if x == target:
                # Moving from curr to curr + 1 means all prefixes equal to curr
                # now become strictly less than the new prefix sum
                less_count += freq[curr]
                curr += 1
            else:
                # Moving from curr to curr - 1 means all prefixes equal to curr - 1
                # are no longer strictly less than the new prefix sum
                curr -= 1
                less_count -= freq[curr]
                
            ans += less_count
            freq[curr] += 1
            
        return ans