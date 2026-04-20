"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort by start time all the intervals
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x.start, x.end))
        minheap = []

        for index in range(len(intervals)):
            if minheap and minheap[0] <= intervals[index].start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, intervals[index].end)

        return len(minheap)









            







        