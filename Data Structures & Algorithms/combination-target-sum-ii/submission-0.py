class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        No duplicate elements so we choose it or we don't and then we move on
        '''
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            # i should be the next
            for j in range(i, len(candidates)):
                # can't have duplicate values
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    break
                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()
        
        dfs(0, [], 0)
        return res