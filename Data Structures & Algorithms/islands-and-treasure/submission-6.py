class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()
        distance = 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append([row, col])

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nrow, ncol = dr + row, dc + col
                    if nrow < 0 or nrow == ROWS or ncol < 0 or ncol == COLS or (nrow, ncol) in visit or grid[nrow][ncol] == -1 or grid[nrow][ncol] == 0:
                        continue
                    grid[nrow][ncol] = distance
                    visit.add((nrow, ncol))
                    q.append([nrow, ncol])
            distance += 1

        

        





        

                    

        