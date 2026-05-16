class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        we do a decision tree of chosing one of the next index's until
        it exceeds the target value, then we just continue in the loop

        at each iteration, try itself up to the max value
        '''
        res = []
        nums.sort()

        def dfs(i, cur, total):
            # ideal case
            if total == target:
                res.append(cur.copy())
                return
            # allows for duplicates until we exceed
            for j in range(i, len(nums)):
                # exceeded
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        dfs(0, [], 0)
        return res
        
