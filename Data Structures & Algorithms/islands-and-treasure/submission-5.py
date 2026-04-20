class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        visit = set()
        dist = 1
        directions = [[-1, 0],[1, 0], [0, 1], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visit.add((row, col))
        
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or (nr, nc) in visit or grid[nr][nc] == 0 or grid[nr][nc] == -1:
                        continue
                    grid[nr][nc] = dist
                    visit.add((nr, nc))
                    q.append((nr, nc))
            dist += 1

        

                    

        