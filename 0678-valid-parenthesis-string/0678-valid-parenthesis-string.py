class Solution(object):
    def checkValidString(self, s):
        bal = 0
        for c in s:
            if c == ')':
                bal -= 1
                if bal < 0:
                    return False
            else:
                bal += 1

        bal = 0
        for c in reversed(s):
            if c == '(':
                bal -= 1
                if bal < 0:
                    return False
            else:
                bal += 1

        return True