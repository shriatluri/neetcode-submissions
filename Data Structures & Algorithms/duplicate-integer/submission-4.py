class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodups = set()

        for i in range(len(nums)):
            if nums[i] in nodups:
                return True
            nodups.add(nums[i])
        return False