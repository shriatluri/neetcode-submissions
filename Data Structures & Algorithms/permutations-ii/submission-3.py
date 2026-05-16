class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        There might be duplicates, return them in any order, just skip
        if the next value is the same, use previous prem logic
        '''
        nums.sort()
        res = []

        # just i, nums is being altered and all we need is the index
        def dfs(i):
            # if j same as j-1 then just keep going, don't swap
            if i == len(nums):
                res.append(nums.copy())
                return
            seen = set()
            for j in range(i, len(nums)):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])
                # if not, we can swap
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                # swap back all of the ones 
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return res