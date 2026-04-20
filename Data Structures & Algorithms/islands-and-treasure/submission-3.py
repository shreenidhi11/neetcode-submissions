class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        distance = 0
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visit.add((r, c))
        
        while queue:
            distance += 1
            for _ in range(len(queue)):
                row, col  = queue.popleft()
                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc
                    if nrow < 0 or nrow == ROWS or ncol < 0 or ncol == COLS or (nrow, ncol) in visit or grid[nrow][ncol] == -1:
                        continue

                    visit.add((nrow, ncol))
                    queue.append((nrow, ncol))
                    grid[nrow][ncol] = distance



    #tc is m*n
    #sc is m * n


        