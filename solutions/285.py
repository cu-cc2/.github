# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Approach 1: Iterative BST Traversal (Optimal - O(h) Time, O(1) Space)
class Solution:
    def inorderSuccessor(self, root, p):
        """
        Find the in-order successor of node p in a Binary Search Tree.

        The in-order successor is the node with the smallest value greater than p.val.

        Args:
            root: The root of the BST
            p: The target node whose successor we need to find

        Returns:
            The in-order successor node, or None if it doesn't exist
        """
        successor = None

        # Traverse the BST from root
        while root:
            if root.val > p.val:
                # Current node's value is greater than p's value
                # This could be a potential successor
                successor = root
                # Look for a smaller successor in the left subtree
                root = root.left
            else:
                # Current node's value is less than or equal to p's value
                # The successor must be in the right subtree
                root = root.right

        return successor


# Approach 2: Recursive BST Traversal
class SolutionRecursive:
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root
