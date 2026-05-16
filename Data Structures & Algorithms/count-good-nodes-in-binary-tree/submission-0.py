# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        This will be a reccursive dfs
        Keep track of the values in the path
        The path value will be the highest value in the path so far
        if cur node val is > than max_path_val, increment count and then change max_val_path 
        '''
        if not root:
            return 0
        self.count = 0

        def dfs(node, max_val_path):
            if not node:
                return
            if node.val >= max_val_path:
                max_val_path = node.val
                self.count += 1
            dfs(node.left, max_val_path)
            dfs(node.right, max_val_path)
        dfs(root, -101)
        return self.count
            


