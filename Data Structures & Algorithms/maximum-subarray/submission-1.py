class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n), O(1)
        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            # check to reset or not
            cur_sum = max(cur_sum, 0)
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
        return max_sum
