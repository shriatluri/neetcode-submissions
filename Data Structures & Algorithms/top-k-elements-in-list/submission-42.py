from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numberDict = defaultdict(int)
        bucketDict = {}
        result = []

        for num in nums:
            numberDict[num] += 1

        for i in range(len(nums) + 1):
            bucketDict[i] = []
        
        for num, freq in numberDict.items():
            bucketDict[freq].append(num)
        
        for i in range(len(bucketDict) - 1, -1, -1):
            for num in bucketDict[i]:
                result.append(num)
                if len(result) == k:
                    return result
            



            

