class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if nums[i] == nums[j] and the distance between them is <= k return true
        mapping = {}
        for i in range(len(nums)):
            # check the last time that the mapping happened
            if nums[i] in mapping and i - mapping[nums[i]] <= k:
                return True
            # number -> location
            mapping[nums[i]] = i
        return False