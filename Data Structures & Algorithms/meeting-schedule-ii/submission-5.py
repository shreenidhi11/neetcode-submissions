"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minheap = []
        # intervals.sort()



        newintervals =  [[i.start,i.end] for i in intervals]

        newintervals.sort()

        for start,end in newintervals:
            if minheap and minheap[0] <= start:
                heapq.heappop(minheap)
                heapq.heappush(minheap,end)
            elif minheap and minheap[0] > start:
                heapq.heappush(minheap,end)
            else:
                heapq.heappush(minheap,end)


        return len(minheap)
















            




        