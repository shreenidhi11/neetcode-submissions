class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start,end  = newInterval[0], newInterval[1]
        res= []
        # start is 2 and end is 5

        for i in range(len(intervals)):

            if end < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif start > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0],newInterval[0]), max(intervals[i][1],newInterval[1])]
            
        res.append(newInterval)
        return res







        