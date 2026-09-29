class Solution:
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        count = [0] * 26

        for ch in s:
            count[ord(ch) - 97] += 1

        ans = []

        for i in range(n):
            t = ord(target[i]) - 97

            # Try to keep equal
            if count[t] > 0:
                count[t] -= 1
                ans.append(target[i])
                continue

            # Try a character greater than target[i]
            for c in range(t + 1, 26):
                if count[c] > 0:
                    count[c] -= 1
                    ans.append(chr(c + 97))

                    for x in range(26):
                        ans.append(chr(x + 97) * count[x])

                    return "".join(ans)

            break

        # Target was completely matched.
        # Backtrack to find the rightmost position we can increase.
        while ans:
            old = ans.pop()
            count[ord(old) - 97] += 1

            prev = ord(old) - 97

            for c in range(prev + 1, 26):
                if count[c] > 0:
                    count[c] -= 1
                    ans.append(chr(c + 97))

                    for x in range(26):
                        ans.append(chr(x + 97) * count[x])

                    return "".join(ans)

        return ""