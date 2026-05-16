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
        # put in array with in order traversal
        arr = []

        def inorder(node):
            # if None, you can't add
            if not node:
                return
            # go all the way to the left, comes back up
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return arr[k - 1]
            
            
            