class Solution:
    def createBinaryTree(self, descriptions):
        nodes = {}
        children = set()

        for p, c, isLeft in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)

            if isLeft:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            children.add(c)

        for val in nodes:
            if val not in children:
                return nodes[val]