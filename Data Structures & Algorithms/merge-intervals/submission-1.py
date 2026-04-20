class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            print(start,end)
            last = output[-1][1]
            print(last)

            if start > last:
                output.append([start,end])

            else:
                # merge the interval
                # here last output value is getting updated only right with
                # new values
                output[-1] = [min(start,output[-1][0]), max(end,output[-1][1])]
        return output


            




















        