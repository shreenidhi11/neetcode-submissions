class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()

        ending = intervals[0][1]


        for start, end in intervals[1:]:
            if start >= ending:
                ending = end
                
            else:
                res+=1
                ending = min(ending,end)

        return res












        