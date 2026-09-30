class Solution:
    def numberOfSpecialChars(self, word):
        last_lower = [-1] * 26
        first_upper = [len(word)] * 26

        for i, ch in enumerate(word):
            if 'a' <= ch <= 'z':
                last_lower[ord(ch) - 97] = i
            else:
                first_upper[ord(ch) - 65] = min(
                    first_upper[ord(ch) - 65], i
                )

        ans = 0

        for i in range(26):
            if (last_lower[i] != -1 and
                first_upper[i] != len(word) and
                last_lower[i] < first_upper[i]):
                ans += 1

        return ans