class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        #i is index, n is number: key & val
        for i,n in enumerate(nums):
            dif = target - n
            if dif in dic:
                return[dic[dif], i]
            dic[n] = i