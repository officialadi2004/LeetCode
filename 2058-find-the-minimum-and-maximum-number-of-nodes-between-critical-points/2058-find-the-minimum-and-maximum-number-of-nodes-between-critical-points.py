
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        first = last = -1
        min_dist = float('inf')
        i = 1

        while curr.next:
            a, b, c = prev.val, curr.val, curr.next.val

            if (b - a) * (b - c) > 0:
                if first == -1:
                    first = i
                else:
                    min_dist = min(min_dist, i - last)
                last = i

            prev = curr
            curr = curr.next
            i += 1

        if first == last:
            return [-1, -1]

        return [min_dist, last - first]
