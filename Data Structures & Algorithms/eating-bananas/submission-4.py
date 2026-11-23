import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        # keep going smaller until 
        while l <= r:
            mid = (r + l) // 2

            tempH = 0
            for pile in piles:
                tempH += math.ceil(pile / mid)
            
            if tempH > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
