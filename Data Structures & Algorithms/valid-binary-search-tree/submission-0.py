# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function is needed to check the left and right with DFS
        def valid(node, left, right):
            # Base case
            if not node:
                return True
            # Condition
            if not left < node.val < right:
                return False
    
            # check the left node and right node
            # left is same for left, right is same for right
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        # Start with OG root
        return valid(root, float('-inf'), float('inf'))