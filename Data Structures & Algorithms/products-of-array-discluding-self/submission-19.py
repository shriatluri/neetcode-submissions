class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            val = 1
            for j in range(n):
                if i == j:
                    continue
                val *= nums[j]
            res[i] = val
        return res
