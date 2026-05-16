class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hashMap:
                return [hashMap[dif], i]
            hashMap[n] = i