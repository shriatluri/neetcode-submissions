class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            # total hours if k = mid
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            # if small, try to take less time
            if hours <= h:
                res = min(k, res)
                r = k - 1
            # if large, try to take more time
            else:
                l = k + 1
        return res