"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = 0
        e = 0
        count, maxCount = 0, 0
        while e < len(end) and s < len(start):
            if start[s] < end[e]:
                count +=1
                s += 1
            else:
                count -= 1
                e +=1
            maxCount = max(count,maxCount)
        
        return maxCount
