class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #sort the input array
        nums.sort()

        for i, n in enumerate(nums):
            #if same as previous number, continue
            if i > 0 and n == nums[i-1]:
                continue
            #two pointer solution
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    #update one pointer
                    #other pointer will be taken care of
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res