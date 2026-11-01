class Solution:
    def largestAltitude(self, gain):
        curr = highest = 0

        for x in gain:
            curr += x
            if curr > highest:
                highest = curr

        return highest