class Solution(object):
    def mapWordWeights(self, words, weights):
        res = []
        for word in words:
            total_weight = sum(weights[ord(c) - 97] for c in word)
            rem = total_weight % 26
            res.append(chr(122 - rem))
        return "".join(res)