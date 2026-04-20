class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0],[1, 0], [0, 1], [0, -1]]
        visit = set()
        res = 0

        def helper(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or grid[r][c] != "1":
                return
            visit.add((r, c))
            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == "1":
                    helper(r, c)
                    res += 1

        return res

        