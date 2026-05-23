"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x : x.start)
        rooms = []
        for index in range(len(intervals)):
            if rooms and rooms[0] <= intervals[index].start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[index].end)

        return len(rooms)

        # tc is nlogn
        # sc is n






        