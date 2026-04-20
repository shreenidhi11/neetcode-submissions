class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [i * (-1) for i in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            n1 = -heapq.heappop(maxheap)
            n2 = -heapq.heappop(maxheap)

            if n1 != n2:
                heapq.heappush(maxheap, -(n1-n2))
 
        return -maxheap[0] if maxheap else 0

        
        
        








        
        

        