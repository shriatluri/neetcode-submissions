# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        # Check if identical: returns True
        if self.isIdentical(root, subRoot):
            return True
        
        # either the left or right, can't be both
        return (self.isSubtree(root.right, subRoot) or
                self.isSubtree(root.left, subRoot))

    # Helper function to check if identical: DFS
    def isIdentical(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case
        if not root and not subRoot:
            return True
        # DFS through tree
        if root and subRoot and root.val == subRoot.val:
            return self.isIdentical(root.right, subRoot.right) and self.isIdentical(root.left, subRoot.left)
        # If we dont get to base case
        return False