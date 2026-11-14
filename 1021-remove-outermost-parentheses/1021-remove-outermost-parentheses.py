class Solution(object):
    def removeOuterParentheses(self, s):
        res = []
        depth = 0
        start = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                if depth == 0:
                    start = i
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    res.append(s[start + 1 : i])
                    
        return "".join(res)