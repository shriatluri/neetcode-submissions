class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num - 1) not in numset:
                curlen = 1
                while (num + curlen) in numset:
                    curlen += 1
                longest = max(longest, curlen)
        return longest