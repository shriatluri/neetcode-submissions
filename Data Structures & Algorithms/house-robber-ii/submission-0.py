class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])

        def robba(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return max(nums[0],nums[1])
            
            dp = [0] * (len(nums))
            # each entry in the dp table will be the maximum amount 
            # of money that can be robbed to taht house
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = max(nums[1], nums[0] + nums[2])
            for i in range(3, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1], dp[i-3] + nums[i])
            print(dp)
            return dp[-1]
        return max(robba(nums[:-1]), robba(nums[1:]))
        