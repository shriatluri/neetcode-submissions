class Solution:
    '''
    There will be a value that occurs more than n // 2 times -> Takes away edge cases
    
    Keep track of the max with just one element. Res and Count
    Everytime you see a val that is not the res, you can recrement by 1
    Once the count becomes 0 we MIGHT have a different result

    Ex: [2,2,1,1,1,2,2]
    res = 2 2 2 2 1 1 2
    count = 1 2 1 0 1 0 1

    DP basically, DP[i] = the max element in that part of the array
    '''
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0

        for num in nums:
            # we might have a new candidate
            if count == 0:
                res = num
            # always increment count
            count += (1 if num == res else -1)
        return res
        