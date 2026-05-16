class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by the first number
        intervals.sort(key = lambda x : x[0])

        output = []
        for i in range(len(intervals)):
            if output and intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(intervals[i][1], output[-1][1])
            else:
                output.append(intervals[i])
        return output