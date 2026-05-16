class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        All number have to be in the array, it is a reordering of the nubers
        We need to use the swap methodology where we start with original nums

        '''
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(nums[0:i])
                return
            for j in range(i, len(nums)):
                # swap and upswap
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                # swap back
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return res