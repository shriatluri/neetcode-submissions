class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_count = 0
        for i in range(len(nums)):
            count = 0
            if nums[i] - 1 not in nums:
                count += 1
                while nums[i] + count in nums:
                    count += 1
                
                if count > max_count:
                    max_count = count
                
            
        return max_count
