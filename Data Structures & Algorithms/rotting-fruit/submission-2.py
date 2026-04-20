class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0],[1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()
        fresh = 0

        # first count the number of treasure chest
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))

                elif grid[r][c] == 1:
                    fresh += 1



        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = dr + row, dc + col
                    if newRow < 0 or newRow == ROWS or newCol < 0 or newCol == COLS or (newRow, newCol) in visit or grid[newRow][newCol] != 1:
                        continue
                    visit.add((newRow, newCol))
                    q.append((newRow, newCol))
                    grid[newRow][newCol] = 2
                    fresh -= 1
            time += 1
                    

        return time if fresh == 0 else -1

        