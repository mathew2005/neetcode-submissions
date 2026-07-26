"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        
        prev, curr = 0, 1
        while curr < len(intervals):
            if intervals[prev].end > intervals[curr].start:
                return False
            prev += 1
            curr += 1
        
        return True