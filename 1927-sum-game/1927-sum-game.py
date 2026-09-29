class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        diff = 0
        q = 0

        for i in range(n):
            if num[i] == '?':
                if i < half:
                    q += 1
                else:
                    q -= 1
            else:
                digit = ord(num[i]) - 48
                if i < half:
                    diff += digit
                else:
                    diff -= digit

        # Odd difference in number of '?' -> Alice wins
        if q % 2 != 0:
            return True

        # Bob wins only if the sums can be perfectly balanced
        return 2 * diff != -9 * q