"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        starts = [intervals[i].start for i in range(n)]
        ends = [intervals[i].end for i in range(n)]
        starts.sort()
        ends.sort()


        res = 0 
        ptr= 0

        for start in starts:

            if start < ends[ptr]:
                res +=1 

            else:
                ptr +=1

        return res






        



       