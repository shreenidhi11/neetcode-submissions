class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastindex = {} #char->lastindex


        # keep track of last indexes
        for i,ch in enumerate(s):
            lastindex[ch] = i

        # initialize variables
        size = 0
        end = 0
        res= []

        # abcabc
        # a: 3, b: 4, c: 5
        for i, ch in enumerate(s):
            size+=1
            end = max(end, lastindex[ch])

            if i == end:
                res.append(size)
                size = 0

        return res




        

        