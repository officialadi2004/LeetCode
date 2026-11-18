class Solution(object):
    def averageOfSubtree(self, root):
        ans = [0]

        def dfs(node):
            total = node.val
            cnt = 1
            if node.left:
                ls, lc = dfs(node.left)
                total += ls
                cnt += lc
            if node.right:
                rs, rc = dfs(node.right)
                total += rs
                cnt += rc
            if total // cnt == node.val:
                ans[0] += 1
            return total, cnt

        dfs(root)
        return ans[0]