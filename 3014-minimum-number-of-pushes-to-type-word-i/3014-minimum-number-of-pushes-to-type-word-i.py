class Solution(object):
    def minimumPushes(self, word):
        n = len(word)
        full_rounds = n // 8
        remainder = n % 8
        
        pushes = 8 * (full_rounds * (full_rounds + 1) // 2)
        pushes += remainder * (full_rounds + 1)
        
        return pushes