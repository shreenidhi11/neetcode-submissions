class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        vis = set()
        q = deque()
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]  == 0:
                    q.append((r,c))
                    vis.add((r,c))

        dist = 0
        while q:
            dist+=1
            for _ in range(len(q)):

                r,c = q.popleft()
                # vis.add((r,c))
                # iteraitng the directions
                for dr,dc in directions:
                    row, col = r+dr, c + dc
                    if row < 0 or row == ROWS or col < 0 or col == COLS or (row,col) in vis or grid[row][col] == -1 :
                        continue

                    grid[row][col] = dist
                    vis.add((row,col))
                    q.append((row,col))


        # return grid


                    


        
        


        


        



        








        












        