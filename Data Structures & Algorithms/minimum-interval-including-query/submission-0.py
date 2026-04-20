class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minheap = []
        res = {}
        i = 0

        for q in sorted(queries):
            # add all the related intervals in the minheap in the below format
            # (length, right value)
            # why right because because that is the boundary limit for
            # each query
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minheap, (r-l+1,r))
                i+=1

            # Now remove all the unwanted intervals for this q.
            while minheap and minheap[0][1] < q:
                    heapq.heappop(minheap)

            # add the length of the interval that is small else -1
            res[q] = minheap[0][0] if minheap else  -1

        return [res[q] for q in queries]



        