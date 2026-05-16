class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Decision tree method with backtracking
        Need to account for those duplicate values
        Runtime: O()
        '''
        res = []
        nums.sort()

        # recusive function to find all valid combinations
        # index we are on, cur array, total_sum
        def dfs(i, cur, total):
            # base case
            if total == target:
                res.append(cur.copy())
                return
            # i because we can repeat values
            for k in range(i, len(nums)):
                # can't have
                if total + nums[k] > target:
                    return
                cur.append(nums[k])
                # new start index
                dfs(k, cur, total + nums[k])
                # try with other values in the remainder of the array
                cur.pop()
        dfs(0, [], 0)
        return res

    

            
