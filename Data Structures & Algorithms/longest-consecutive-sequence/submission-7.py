class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        count = 0
        max_count = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                if length > max_count:
                    max_count = length
            
        return max_count
            
            
