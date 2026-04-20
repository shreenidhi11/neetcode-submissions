class MedianFinder:

    def __init__(self):
        self.small = [] #this will be a maxheap
        self.large = [] #this will be a minheap
        
    def addNum(self, num: int) -> None:
        # the size of the small heap and the large heap should
        # be almost the same. And the max element from small heap
        # should be greater than the min element in the large heap
        # if not then we move from small to large

        # By default add to small heap [2,4,5,3]
        heapq.heappush(self.small, -1*num)

        # need to make sure that all the numbers in small heap is 
        # smaller than large heap
        if (self.large and self.small
         and -1 * self.small[0] > self.large[0]):
           val = -1* heapq.heappop(self.small)
           heapq.heappush(self.large, val)

        # uneven size
        if len(self.small) > len(self.large)+1:
           val = -1* heapq.heappop(self.small)
           heapq.heappush(self.large, val)
        if len(self.large) > len(self.small)+1:
           val = heapq.heappop(self.large)
           heapq.heappush(self.small, -1* val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return  self.large[0]
        else: 
            return (-1*self.small[0] + self.large[0]) / 2



        