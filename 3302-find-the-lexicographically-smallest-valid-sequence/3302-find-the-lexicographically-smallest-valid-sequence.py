class Solution:
    def validSequence(self, word1, word2):
        n, m = len(word1), len(word2)
        suf = [-1] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if word1[i] == word2[j]:
                suf[j] = i
                j -= 1
                if j < 0:
                    break

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and (
                j == m - 1 or
                (suf[j + 1] != -1 and i < suf[j + 1])
            ):
                ans.append(i)
                changed = True
                j += 1

        return ans if j == m else []