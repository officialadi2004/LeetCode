class Solution:
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x:
            result = result * 10 + x % 10
            x //= 10

        result *= sign

        if result < -2147483648 or result > 2147483647:
            return 0

        return result