import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Your objective for this problem is to eat as slow as possible
        and finish all of the bananas in the pile.

        The largest pile matters as you are "restricted" by this
        '''
        max_speed = max(piles)
        l, r = 1, max_speed
        res = r
        while l <= r:
            k = (l + r) // 2
            # Lets see how low we can go
            totalTime = 0
            # get total time for each of the runs with new k
            for n in piles:
                totalTime += math.ceil(n / k)
            # if we have more time left, we can go slower
            if totalTime <= h:
                res = k
                r = k - 1
            # We went over the time, need to speed up
            else:
                l = k + 1
        return res
            