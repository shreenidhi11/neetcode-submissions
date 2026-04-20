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

        newintervals =  [[i.start,i.end] for i in intervals]
        newintervals.sort()

        minheap = []
        minheap.append(newintervals[0][1])

        for index in range(1, len(newintervals)):
            if minheap:
                if minheap[0] <= newintervals[index][0]:
                    # earliest ending meeting
                    heapq.heappop(minheap)
                    # heapq.heappush(minheap, newintervals[index][1])
            heapq.heappush(minheap, newintervals[index][1])
            
        return len(minheap)

            







        