class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by the start value
        intervals.sort(key = lambda i : i[0])
        # put the merged intervals, start w first interval
        output = [intervals[0]]
        #start from first interval, get start & end value
        for start, end in intervals[1:]:
            # most recently added interval and its end value
            lastEnd = output[-1][1]
            #if overlap
            if start <= lastEnd:
                #merge; value of most recently added interval and its end value,
                #equal to the max of the last end value and the current end value
                output[-1][1] = max(lastEnd, end)
            #if not overlapping, add interval to output
            else:
                output.append([start, end])
        return output