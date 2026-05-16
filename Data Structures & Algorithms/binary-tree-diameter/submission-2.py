# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # val at a current node should be its max height
        self.res = 0
        # calculating the height at the node we are at
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left + right)
            # returning height of the current node
            return 1 + max(left, right)
        dfs(root)
        return self.res