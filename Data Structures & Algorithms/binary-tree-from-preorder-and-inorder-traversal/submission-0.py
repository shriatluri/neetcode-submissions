# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        You are given pre-order and in-order traversals -> show tree
        Preorder: NLR
        Inorder: LNR

        Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
        Output: [1,2,3,null,null,null,4]
        
        Logic: Preorder first value is node
        So the strategy is:
        1. The first element in preorder is always the root.
        2. Find that roots index in the inorder list.
        3. Everything left of that index in inorder is the left subtree; everything right is the right subtree.
        4. Recursively build the left and right subtrees by slicing the preorder and inorder arrays accordingly.

        O(n) time, O()
        '''
        # map each value -> in-order index for O(1) look-up
        indeces = {val: i for i, val in enumerate(inorder)}
        self.pre_index = 0

        def dfs(l, r):
            # base case, left index can't be more than right
            if l > r:
                return None
            # location of root in pre order
            root_val = preorder[self.pre_index]
            # next node in inorder
            self.pre_index += 1
            # return the root, top to bottom, level order
            root = TreeNode(root_val)
            # Subtree splitting, mid and then left and right subtree root
            mid = indeces[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)
            


        

