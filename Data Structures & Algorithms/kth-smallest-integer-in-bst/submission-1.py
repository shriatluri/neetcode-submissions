# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        In order traversal with a counter, left, node right
        '''
        arr = []
        def inorder(node):
            # base case in call stack
            if not node:
                return None
            # inorder traversal
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        # 1 indexed
        return arr[k-1]