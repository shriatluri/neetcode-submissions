# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        node = root
        q = deque()

        if not root:
            return None

        q.append(root)

        while q:
            popNode = q.popleft()
            popNode.left, popNode.right = popNode.right, popNode.left
            if popNode.left:
                q.append(popNode.left)
            if popNode.right:
                q.append(popNode.right)
        
        return node
            

            