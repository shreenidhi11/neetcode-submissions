class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0],[1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()


        # first count the number of treasure chest
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))


        # def bfs(r, c):
        #     visit.add((r, c))
        #     q.append((r, c))
        #     area = 1
        dist = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = dr + row, dc + col
                    if newRow < 0 or newRow == ROWS or newCol < 0 or newCol == COLS or (newRow, newCol) in visit or grid[newRow][newCol] == -1:
                        continue
                    visit.add((newRow, newCol))
                    q.append((newRow, newCol))
                    grid[newRow][newCol] = dist
            dist += 1
                    

        # return grid

        