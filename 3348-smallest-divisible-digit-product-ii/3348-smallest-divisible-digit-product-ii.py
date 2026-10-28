
class Solution:
    def smallestNumber(self, num, t):
        factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0)
        }

        need = [0, 0, 0, 0]
        for idx, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                need[idx] += 1
                t //= p

        if t != 1:
            return "-1"

        def min_digits(a, b, c, d):
            best = 10**9
            for sixes in range(min(a, b, 5) + 1):
                count = (
                    sixes
                    + (a - sixes + 2) // 3
                    + (b - sixes + 1) // 2
                    + c + d
                )
                best = min(best, count)
            return best

        def build_suffix(req, length):
            result = []

            for i in range(length):
                for digit in range(1, 10):
                    f = factors[digit]
                    rem = [
                        max(0, req[j] - f[j])
                        for j in range(4)
                    ]

                    if min_digits(*rem) <= length - i - 1:
                        result.append(str(digit))
                        req = rem
                        break

            return ''.join(result)

        # Check whether num itself is valid.
        if '0' not in num:
            have = [0, 0, 0, 0]

            for ch in num:
                f = factors[int(ch)]
                for j in range(4):
                    have[j] += f[j]

            if all(have[j] >= need[j] for j in range(4)):
                return num

        # Only prefixes before the first zero can be kept unchanged.
        zero_pos = num.find('0')
        start = zero_pos if zero_pos != -1 else len(num) - 1

        prefix = [0, 0, 0, 0]
        for ch in num[:start]:
            f = factors[int(ch)]
            for j in range(4):
                prefix[j] += f[j]

        for i in range(start, -1, -1):
            current = int(num[i])
            suffix_len = len(num) - i - 1

            for digit in range(current + 1, 10):
                f = factors[digit]
                rem = [
                    max(0, need[j] - prefix[j] - f[j])
                    for j in range(4)
                ]

                if min_digits(*rem) <= suffix_len:
                    suffix = build_suffix(rem, suffix_len)
                    return num[:i] + str(digit) + suffix

            if i > 0:
                f = factors[int(num[i - 1])]
                for j in range(4):
                    prefix[j] -= f[j]

        # No valid answer of the same length: use a longer number.
        length = max(len(num) + 1, min_digits(*need))
        return build_suffix(need, length)
