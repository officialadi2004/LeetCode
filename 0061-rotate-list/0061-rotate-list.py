class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Rotating length times gives the same list
        k %= length

        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find new tail
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head is after new tail
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head