class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()

        def addroom(r,c):
            if r < 0 or c < 0 or r == rows or c==cols or grid[r][c] == -1 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append([r,c])


        # for loop to find the gates, if found add it to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        dist = 0
        # now process each cell that were added to the queue
        while q:
            for cell in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                # the below 4 functions will only mark the cell that can be reached from
                # the current popped cell
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)

                # by the time we reach here the queue will have new nodes that can be reached
            dist+=1











        