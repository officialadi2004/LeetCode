class Solution:
    def minimumPushes(self, word):
        freq = sorted(__import__('collections').Counter(word).values(), reverse=True)
        
        return sum(f * (i // 8 + 1) for i, f in enumerate(freq))