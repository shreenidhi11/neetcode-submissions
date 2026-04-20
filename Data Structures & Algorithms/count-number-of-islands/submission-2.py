class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0],[1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()
        res = 0

        def bfs(r, c):
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = dr + row, dc + col
                    if newRow < 0 or newRow == ROWS or newCol < 0 or newCol == COLS or (newRow, newCol) in visit or grid[newRow][newCol] != "1":
                        continue
                    visit.add((newRow, newCol))
                    q.append((newRow, newCol))



        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    res += 1

        return res


        