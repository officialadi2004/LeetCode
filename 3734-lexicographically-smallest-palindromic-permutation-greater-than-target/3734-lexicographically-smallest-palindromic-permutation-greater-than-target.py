class Solution:
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        h = n // 2

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Check if palindrome is possible
        odd = 0
        mid = ''

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                mid = chr(i + 97)

        if odd > 1:
            return ""

        # Characters available in the left half
        half_cnt = [x // 2 for x in cnt]

        def make_pal(left):
            left = ''.join(left)
            if n % 2:
                return left + mid + left[::-1]
            return left + left[::-1]

        left = []
        rem = half_cnt[:]

        # Try to make left half equal to target's left half
        for i in range(h):
            t = ord(target[i]) - 97

            if rem[t] > 0:
                rem[t] -= 1
                left.append(target[i])
            else:
                # Try the smallest character greater than target[i]
                bigger = -1

                for c in range(t + 1, 26):
                    if rem[c] > 0:
                        bigger = c
                        break

                if bigger != -1:
                    rem[bigger] -= 1

                    result = left + [chr(bigger + 97)]

                    for c in range(26):
                        result.extend([chr(c + 97)] * rem[c])

                    return make_pal(result)

                # Cannot continue -> backtrack
                break
        else:
            # Entire left half matched target
            candidate = make_pal(left)

            if candidate > target:
                return candidate

        # Backtrack to find the smallest possible larger prefix
        for i in range(len(left) - 1, -1, -1):
            # Put back the character at position i
            old = ord(left[i]) - 97
            rem[old] += 1

            # Try the smallest character greater than it
            for c in range(old + 1, 26):
                if rem[c] > 0:
                    rem[c] -= 1

                    result = left[:i] + [chr(c + 97)]

                    # Remaining characters in sorted order
                    for x in range(26):
                        result.extend([chr(x + 97)] * rem[x])

                    return make_pal(result)

        return ""