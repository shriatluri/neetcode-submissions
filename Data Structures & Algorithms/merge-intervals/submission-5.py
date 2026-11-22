class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1, 1, 6
        # 3, 5, 7
        intervals.sort(key=lambda pair:pair[0])
        result = [intervals[0]]

        for start, end in intervals:
            mostRecentStart = result[-1][0]
            mostRecentEnd = result[-1][1]

            if start >= mostRecentStart and start <= mostRecentEnd:
                newInterval = [min(start, mostRecentStart), max(end, mostRecentEnd)]
                result.pop()
                result.append(newInterval)
            else:
                result.append([start, end])
        
        return result

