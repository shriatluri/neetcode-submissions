class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        if len(nums) == 1:
            return nums[0]

        while r > l:
            # if rightmost element is less than middle
            # minimum must be on the right

            # else
            # minimum must be on the left

            if r - l == 1:
                return min(nums[r], nums[l])
                
            if nums[r] < nums[mid]:
                l = mid
            else:
                r = mid
            
            mid = (l + r) // 2
        
        return mid


            

        