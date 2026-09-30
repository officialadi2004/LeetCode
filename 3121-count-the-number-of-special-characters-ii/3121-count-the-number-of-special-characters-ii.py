class Solution:
    def numberOfSpecialChars(self, word):
        lower = 0
        upper = 0
        invalid = 0

        for ch in word:
            if 'a' <= ch <= 'z':
                bit = 1 << (ord(ch) - 97)

                if upper & bit:
                    invalid |= bit

                lower |= bit
            else:
                bit = 1 << (ord(ch) - 65)
                upper |= bit

        both = lower & upper & ~invalid

        ans = 0
        while both:
            ans += both & 1
            both >>= 1

        return ans