from sortedcontainers import SortedDict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for i, num in enumerate(nums):
            second_num = target - num
            if second_num in hash_map:
                return [hash_map[second_num], i]     
            hash_map[num] = i       