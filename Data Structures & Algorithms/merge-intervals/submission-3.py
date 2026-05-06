class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for start, end in intervals:
            last_end = result[-1][1]
            if start > last_end:
                result.append([start, end])
            else:
                result[-1][1] = max(last_end, end)
                
        return result 


        