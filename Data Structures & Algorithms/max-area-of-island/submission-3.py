class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0
        count = 0
        max_c = 0

        def helper(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or grid[r][c] != 1:
                return 0
            visit.add((r, c))
            return 1 + helper(r + 1, c) + helper(r - 1, c) + helper(r, c + 1) + helper(r, c - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    max_c = max(max_c, helper(r, c))
                    

        return max_c