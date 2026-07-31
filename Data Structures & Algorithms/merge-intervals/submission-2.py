class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2: 
            return intervals

        intervals.sort() # O(nlogn)
        p, c = 0, 1
        while c < len(intervals):

            # case 1: (intervals overlap)
            if intervals[p][1] >= intervals[c][0]:
                intervals[c] = [intervals[p][0], max(intervals[c][1], intervals[p][1])]
                del intervals[p]
                
            else:

                p +=1
                c +=1
        
        return intervals