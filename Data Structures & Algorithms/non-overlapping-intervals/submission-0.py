class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        intervals.sort(key=lambda x : x[0])
        rem = 0 

        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start >= prevEnd:
                prevEnd = end
                 

            else:
                rem +=1
                prevEnd = min(prevEnd, end)

        return rem

