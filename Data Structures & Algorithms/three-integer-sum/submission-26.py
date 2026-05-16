class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            # two pointer
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = nums[l] + nums[r] + n
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    # avoid dups for second number
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res