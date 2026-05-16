import math

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1, 1, 2
        # 2, 4, 2
        intervals.sort()
        prevEnd = -math.inf
        result = 0

        for i, interval in enumerate(intervals):
            if interval[0] < prevEnd:
                prevEnd = min(prevEnd, interval[1])
                result += 1
            else:
                prevEnd = interval[1]
        
        return result