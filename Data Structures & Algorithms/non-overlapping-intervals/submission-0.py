class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        output = [intervals[0]]

        res = 0
        for start, end in intervals[1:]:        
            if start >= output[-1][1]:
                output.append([start,end])
            else:
                res += 1
                output[-1][1] = min(end,output[-1][1])

        return res