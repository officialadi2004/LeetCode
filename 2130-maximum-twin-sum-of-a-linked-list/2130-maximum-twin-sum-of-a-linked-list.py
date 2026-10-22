class Solution:
    def pairSum(self, head):
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        ans = 0

        while slow:
            ans = max(ans, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return ans