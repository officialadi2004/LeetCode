class Solution:
    def braceExpansionII(self, expression):

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                ch = expression[i]

                if ch == '{':
                    part, i = parse(i + 1)

                    new = set()
                    for a in current:
                        for b in part:
                            new.add(a + b)

                    current = new

                elif ch == ',':
                    result |= current
                    current = {""}
                    i += 1

                else:
                    new = set()
                    for word in current:
                        new.add(word + ch)

                    current = new
                    i += 1

            result |= current

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)