class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # go to the sorted side of the array
            
            # left side is sorted
            if nums[l] <= nums[m]:
                # target in sorted section
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # right side is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

