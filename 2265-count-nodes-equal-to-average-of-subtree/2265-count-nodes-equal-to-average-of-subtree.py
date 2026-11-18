class Solution(object):
    def averageOfSubtree(self, root):
        self.ans = 0
        MASK = 1023  # (1 << 10) - 1, since n <= 1000 < 1024

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            total = (l >> 10) + (r >> 10) + node.val
            cnt = (l & MASK) + (r & MASK) + 1
            if total // cnt == node.val:
                self.ans += 1
            return (total << 10) | cnt

        dfs(root)
        return self.ans