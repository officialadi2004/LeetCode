class Solution(object):
    def countCommas(self, n):
        # Numbers with 4 to 6 digits have 1 comma (>= 1,000)
        # Numbers with 7 to 9 digits have 2 commas (>= 1,000,000)
        # Numbers with 10 to 12 digits have 3 commas (>= 1,000,000,000)
        ans = 0
        threshold = 1000
        while n >= threshold:
            ans += n - threshold + 1
            threshold *= 1000
        return ans