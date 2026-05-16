class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1 for i in range(len(nums))]
        preProduct = nums[0]
        for i in range(1, len(nums)):
            res[i] *= preProduct
            preProduct *= nums[i]
        
        postProduct = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= postProduct
            postProduct *= nums[i]
        
        return res





            
