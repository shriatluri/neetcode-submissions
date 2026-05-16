class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            #check if is the start of a sequence
            if (n-1) not in numSet:
                length = 1
                #keep going until sequence ends
                while (n + length) in numSet:
                    length += 1
                #when the loop ends, check if length > longest 
                #due to multiple sequences
                longest = max(length, longest)
        return longest 