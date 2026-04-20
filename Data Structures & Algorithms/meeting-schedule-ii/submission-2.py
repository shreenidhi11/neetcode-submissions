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
        
        intervals.sort(key=lambda x: x.start)

        minheap = []

        heapq.heappush(minheap, intervals[0].end)

        for obj in intervals[1:]:
            if obj.start >= minheap[0]:
                heapq.heappop(minheap)
            
            heapq.heappush(minheap, obj.end)

        return len(minheap)
            












            




        