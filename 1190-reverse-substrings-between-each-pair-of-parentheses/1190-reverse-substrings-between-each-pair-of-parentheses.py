class Solution:
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch == '(':
                stack.append([])

            elif ch == ')':
                part = stack.pop()
                part.reverse()

                if stack:
                    stack[-1].extend(part)
                else:
                    stack.append(part)

            else:
                if stack:
                    stack[-1].append(ch)
                else:
                    stack.append([ch])

        return ''.join(stack[0])