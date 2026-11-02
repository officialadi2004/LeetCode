class Solution:
    def minimumPushes(self, word):
        freq = [0] * 26

        # Count frequency of each character
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        # Put most frequent characters in positions requiring fewer pushes
        freq.sort(reverse=True)

        pushes = 0

        for i in range(26):
            if freq[i] == 0:
                break

            pushes += freq[i] * (i // 8 + 1)

        return pushes