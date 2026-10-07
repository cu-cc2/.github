class Solution:
    def inorderSuccessor(self, root, p):
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor


class SolutionRecursive:
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root
