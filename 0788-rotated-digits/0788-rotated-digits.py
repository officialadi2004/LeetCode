class Solution:
    def rotatedDigits(self, n):
        good = 0

        for num in range(1, n + 1):
            x = num
            valid = True
            different = False

            while x > 0:
                digit = x % 10

                if digit in (3, 4, 7):
                    valid = False
                    break

                if digit in (2, 5, 6, 9):
                    different = True

                x //= 10

            if valid and different:
                good += 1

        return good