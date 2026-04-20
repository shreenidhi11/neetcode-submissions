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
        intervals.sort(key=lambda x: (x.start, x.end))
        minheap = []
        heapq.heappush(minheap, intervals[0].end)

        for index in range(1, len(intervals)):
            if intervals[index].start >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, intervals[index].end)

        return len(minheap)

            






