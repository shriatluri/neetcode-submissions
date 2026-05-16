from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        # set lookup
        numSet = set()

        result = 0

        for num in nums:
            numSet.add(num)
        
        num = nums[0]

        for num in nums:
            if num - 1 not in numSet:
                count = 0
                currNum = num
                while True:
                    if currNum in numSet:
                        count += 1
                        numSet.remove(currNum)
                    else:
                        break

                    currNum += 1
                
                result = max(result, count)
        
        return result
                







            



        