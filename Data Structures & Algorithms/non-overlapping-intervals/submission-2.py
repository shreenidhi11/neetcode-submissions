class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        current_interval = intervals[0]
        removed_intervals = 0
        for index in range(1, len(intervals)):
            if intervals[index][0] >= current_interval[1]:
                current_interval = intervals[index]
            else:
                removed_intervals += 1
                current_interval[1] = min(current_interval[1], intervals[index][1])
        return removed_intervals
            