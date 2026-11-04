import string

class Solution(object):
    def mapWordWeights(self, words, weights):
        mapping = {c: weights[i] for i, c in enumerate(string.ascii_lowercase)}
        rev_alpha = string.ascii_lowercase[::-1]
        
        res = []
        for word in words:
            total = 0
            for c in word:
                total += mapping[c]
            res.append(rev_alpha[total % 26])
            
        return "".join(res)