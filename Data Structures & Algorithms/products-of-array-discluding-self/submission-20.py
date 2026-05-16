class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we have a prefix and postfix value which store in output array
        # O(n) time and O(1) space with 2 passes
        res = [1] * len(nums)

        prefix = 1
        # prefix and postfix pass
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res