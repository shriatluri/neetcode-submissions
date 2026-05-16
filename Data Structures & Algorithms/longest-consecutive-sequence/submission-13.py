class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longSet = set(nums)
        longest = 0
        for n in longSet:
            # if it is the start of a sequence
            if n - 1 not in longSet:
                length = 1
                while (n+length) in longSet:
                    length += 1
                longest = max(longest, length)
        return longest