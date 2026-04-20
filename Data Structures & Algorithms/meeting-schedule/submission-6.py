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

        listIntervals = []
        for inter in intervals:
            listIntervals.append([inter.start,inter.end])
        listIntervals.sort()   

        start, end = listIntervals[0][0], listIntervals[0][1]

        for s, e in listIntervals[1:]:
            if s < end:
                return False
            else:
                start, end = s, e

        return True
