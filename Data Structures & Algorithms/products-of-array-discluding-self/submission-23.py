class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]
        
        frontToBackProducts = []
        runningProduct = 1

        for num in nums:
            runningProduct *= num
            frontToBackProducts.append(runningProduct)
        
        runningProduct = 1
        backToFrontProducts = [0 for i in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            runningProduct *= nums[i]
            backToFrontProducts[i] = runningProduct


        for i in range(len(nums) - 1, -1, -1):
            if not i + 1 < len(nums):
                result[i] = frontToBackProducts[i - 1]
            elif not i - 1 >= 0:
                result[i] = backToFrontProducts[i + 1]
            else:
                result[i] = frontToBackProducts[i-1] * backToFrontProducts[i+1]
        
        return result
 

