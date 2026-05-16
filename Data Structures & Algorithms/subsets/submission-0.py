class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # the current subset
        curSubset = []
        # ex: [1,2,3] - include or not include at that index
        # backtracking
        def dfs(i):
            # base case past leaf node
            if i >= len(nums):
                res.append(curSubset.copy())
                return
            # include
            curSubset.append(nums[i])
            dfs(i + 1)
            # not include
            curSubset.pop()
            dfs(i + 1)
        dfs(0)
        return res

                 
