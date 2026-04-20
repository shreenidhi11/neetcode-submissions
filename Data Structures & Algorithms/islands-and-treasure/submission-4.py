class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        directions = [[-1, 0],[1, 0], [0, 1], [0, -1]]
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visit.add((row, col))

        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or (nr, nc) in visit or grid[nr][nc] == -1 or grid[nr][nc] == 0 :
                        continue
                    visit.add((nr, nc))
                    grid[nr][nc] = dist
                    q.append((nr, nc))

                    

        