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

        print(listIntervals)
        listIntervals.sort()

        s, e = listIntervals[0][0], listIntervals[0][1]

        print(s,e)

        for intervalObj in range(1, len(listIntervals)):
            if listIntervals[intervalObj][0] < e:
                return False
            else:
                s,e =  listIntervals[intervalObj][0] , listIntervals[intervalObj][1]
        return True




        
