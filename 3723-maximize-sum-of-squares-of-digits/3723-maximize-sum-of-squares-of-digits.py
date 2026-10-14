
class Solution:
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        ans = []

        while sum >= 9:
            ans.append('9')
            sum -= 9

        if sum > 0:
            ans.append(str(sum))

        ans.extend('0' * (num - len(ans)))
        return ''.join(ans)
