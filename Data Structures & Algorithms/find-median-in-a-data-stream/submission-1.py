class MedianFinder:

    def __init__(self): 
        #used for storing minimum values of the stream
        self.maxheap = []
        #used for storing large values
        self.minheap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -1 * num)

        if self.minheap and self.maxheap and -1 * self.maxheap[0] > self.minheap[0]:
            #swap the elements
            pop_from_maxheap = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,pop_from_maxheap)


        #uneven sizes hence balance
        #case 1: maxheap is greater
        if len(self.maxheap) > len(self.minheap) + 1:
            pop_from_maxheap = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,pop_from_maxheap)

        #case 2: minheap us greater
        if len(self.minheap) > len(self.maxheap) + 1:
            pop_from_minheap = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1. * pop_from_minheap)


    def findMedian(self) -> float:
        # odd sizes
        if len(self.maxheap) > len(self.minheap):
            return  - 1 * self.maxheap[0]

        elif len(self.minheap) > len(self.maxheap):
            return  self.minheap[0]
        else:
            return ((- 1 * self.maxheap[0] + self.minheap[0]) / 2.0)
            


        
        