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

        prev_start, prev_end = listIntervals[0][0], listIntervals[0][1]

        for start, end in listIntervals[1:]:
            # all the meetings that start before the previous meeting ends cannot be
            # attended
            if start < prev_end:
                return False
            else:
                prev_start, prev_end = start, end

        return True



