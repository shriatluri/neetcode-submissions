class Solution:
    def findMin(self, nums: List[int]) -> int:
        # obviously a form of binary search, how to we mitigate the rotated aspect
        # There are two sorted sections of the array -> find the point

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
