# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            # if both are greater, right subtree
            if q.val > cur.val and p.val > cur.val:
                cur = cur.right
            # if both less than, left subtree
            elif q.val < cur.val and p.val < cur.val:
                cur = cur.left
            # if split between and close or equal to p or q, return what you are on
            else:
                return cur