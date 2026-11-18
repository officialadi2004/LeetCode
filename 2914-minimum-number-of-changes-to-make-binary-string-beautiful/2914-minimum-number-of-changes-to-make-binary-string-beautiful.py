class Solution(object):
    def minChanges(self, s):
        return sum(s[i] != s[i + 1] for i in xrange(0, len(s), 2))