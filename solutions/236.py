class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node=root, p=p, q=q):
            if not node or node == p or node == q:
                return node
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if left and right:
                return node
            return left or right

        return dfs()


class SolutionDirect:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
