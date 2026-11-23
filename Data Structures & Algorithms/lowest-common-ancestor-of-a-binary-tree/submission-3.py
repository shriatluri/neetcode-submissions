# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pPath = [root]
        qPath = [root]

        stack = [(root, [root])]

        while stack:
            curr, path = stack.pop()

            if curr.left:
                newPath = path + [curr.left]
                stack.append((curr.left, newPath))
                if curr.left == p:
                    pPath = newPath
                elif curr.left == q:
                    qPath = newPath

            if curr.right:
                newPath = path + [curr.right]
                stack.append([curr.right, newPath])
                if curr.right == p:
                    pPath = newPath
                elif curr.right == q:
                    qPath = newPath
        
        result = 1
        print([p.val for p in pPath])
        print([q.val for q in qPath])
        for pIterate, qIterate in zip(pPath, qPath):
            if pIterate.val == qIterate.val:
                result = pIterate
        
        return result
            
            
