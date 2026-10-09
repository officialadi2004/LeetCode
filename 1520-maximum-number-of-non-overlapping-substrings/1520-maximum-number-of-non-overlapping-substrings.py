class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - 97
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]
            i = left

            while i <= right:
                x = ord(s[i]) - 97

                if first[x] < left:
                    right = -1
                    break

                right = max(right, last[x])
                i += 1

            if right != -1:
                intervals.append((left, right))

        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for left, right in intervals:
            if left > end:
                ans.append(s[left:right + 1])
                end = right

        return ans