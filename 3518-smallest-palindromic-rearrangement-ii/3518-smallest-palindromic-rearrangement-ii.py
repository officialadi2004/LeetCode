class Solution:
    def smallestPalindrome(self, s, k):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - 97] += 1

        half = [c // 2 for c in freq]
        n = sum(half)

        def factorial(x):
            result = 1
            for i in range(2, x + 1):
                result *= i
            return result

        ways = factorial(n)

        for c in half:
            ways //= factorial(c)

        if ways < k:
            return ""

        left = []
        remaining = n

        while remaining:
            for i in range(26):
                if half[i] == 0:
                    continue

                # Number of arrangements starting with this character
                count = ways * half[i] // remaining

                if k > count:
                    k -= count
                else:
                    left.append(chr(i + 97))
                    half[i] -= 1
                    ways = count
                    remaining -= 1
                    break

        middle = ""

        for i in range(26):
            if freq[i] % 2:
                middle = chr(i + 97)
                break

        first = ''.join(left)
        return first + middle + first[::-1]