class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_count = 0
        for n in num_set:
            count = 0
            if n - 1 not in num_set:
                count += 1
                while n + count in nums:
                    count += 1
                
                if count > max_count:
                    max_count = count
                
            
        return max_count
