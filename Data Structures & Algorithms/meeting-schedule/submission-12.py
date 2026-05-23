"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        current_interval = intervals[0]
        for index in range(1, len(intervals)):
            if intervals[index].start < current_interval.end:
                return False
            current_interval = intervals[index]
        
        return True
                

