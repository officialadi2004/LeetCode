class Solution:
    def removeInvalidParentheses(self, s):
        def valid(x):
            balance = 0

            for ch in x:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = {s}

        while queue:
            ans = []

            for x in queue:
                if valid(x):
                    ans.append(x)

            if ans:
                return list(set(ans))

            next_queue = set()

            for x in queue:
                for i in range(len(x)):
                    if x[i] in '()':
                        next_queue.add(x[:i] + x[i + 1:])

            queue = next_queue

        return [""]