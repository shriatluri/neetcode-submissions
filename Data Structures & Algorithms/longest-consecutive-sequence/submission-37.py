class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        curSeq = []
        result = 0


        for num in nums:
            if num - 1 not in numsSet:
                curNum = num

                while curNum in numsSet:
                    curSeq.append(curNum)
                    curNum += 1

                result = max(result, len(curSeq))
                curSeq = []
        
        return result


                

            



        