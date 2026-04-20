class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort the intervals
        intervals.sort()
        res = {}
        minheap = []
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minheap,[r-l+1,r])
                # minheap.append([r-l+1,r])
                i+=1

            print(minheap)
            
            while minheap and minheap[0][1] < q:
                    heapq.heappop(minheap)

            if minheap:
                print("for q--->", q)
                print(minheap[0][0])
                res[q] = minheap[0][0]

        print(res)
        
        return [res[q]  if q in res else -1 for q in queries]







        