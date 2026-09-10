class Solution:
    def reverse(self, x):

        result = 0
        sign = 1

        if x < 0:
            sign = -1
            x = -x

        while x > 0:
            digit = x % 10
            x = x // 10

            result = result * 10 + digit

            if result > 2147483647:
                return 0

        return sign * result