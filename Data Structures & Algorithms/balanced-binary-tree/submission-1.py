# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS; bottom to root
        # determine if every subtree is valid (T, height)
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            # Boolean
            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        # return just the boolean, height is for internal reference
        return dfs(root)[0]