class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix and postfix
        res = [1] * len(nums)

        #prefix's first
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        #postfix's next
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res