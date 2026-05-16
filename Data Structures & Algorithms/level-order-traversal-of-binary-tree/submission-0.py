# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Binary tree means that it is either 0, 1, 2 children per node
        As we process a node, process children form left to right
        '''
        # BFS, level order, check left and right children and then add
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            # each level is len of queue
            lenq = len(queue)
            level = []
            for i in range(lenq):
                node = queue.popleft()
                # check if Null or not
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res
            # after we pop, we append into new list, we add children

        