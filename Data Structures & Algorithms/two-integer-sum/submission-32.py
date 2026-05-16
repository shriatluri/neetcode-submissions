class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_int = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in num_to_int:
                return [num_to_int[dif], i]
            num_to_int[n] = i
    