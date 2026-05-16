from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        currLen = 0

        numSet = set(nums)
        
        for num in nums:
            if (num - 1) not in numSet:
                index = num
                while index in numSet:
                    index += 1
                    currLen += 1
                if currLen > maxLen:
                    maxLen = currLen

            currLen = 0
        
        return maxLen
                    
                

            



        