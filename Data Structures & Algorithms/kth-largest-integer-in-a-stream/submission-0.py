class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Use a min heap that should be of size k
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)

        while len(self.minheap) > k:
            # always removes the minimum element
            heapq.heappop(self.minheap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)

        if len(self.minheap) > self.k:
        
            heapq.heappop(self.minheap)
            
        return self.minheap[0]



        
