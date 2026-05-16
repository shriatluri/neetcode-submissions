class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodups = set()

        for n in nums:
            if n not in nodups:
                nodups.add(n)
            else:
                return True
        return False
            