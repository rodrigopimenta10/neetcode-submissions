class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        output = [intervals[0]]

        res = 0
        for start, end in intervals[1:]:
            if start < output[-1][1]:
                res += 1
                output[-1][1] = min(output[-1][1], end)
            else:
                output.append([start,end])

        return res