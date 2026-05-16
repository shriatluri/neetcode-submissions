class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # handle before, interval, after
        i = 0
        length = len(intervals)
        start, end = newInterval[0], newInterval[1]
        res = []

        # before
        while i < length and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1
        
        # during
        while i < length and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        # after
        while i < length:
            res.append(intervals[i])
            i += 1
        return res