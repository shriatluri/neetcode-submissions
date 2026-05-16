class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        Have one pointer at i and one at n, when nums[i] == val, replace with nums n
        0,1,2,2,3,4,5,2
        0,1,3,4,5
                k
        '''
        k = 0
        for i in range(len(nums)):
            # only add when it is not equal to val, skip if is
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k