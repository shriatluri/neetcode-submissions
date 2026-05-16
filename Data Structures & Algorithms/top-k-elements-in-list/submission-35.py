class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {1:1, 2}
        # bucket sort
        countDict = defaultdict(int)
        arr = []
        result = []

        for num in nums:
            countDict[num] += 1
        
        for key, val in countDict.items():
            arr.append([val, key])
        
        arr.sort()

        for i in range(k):
            result.append(arr[-1 - i][1])

        return result



