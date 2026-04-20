class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        visit = set()
        cache = {}
        max_lip = 0

        def dfs(r, c, value):
            # boundary conditions
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or matrix[r][c] <= value:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            visit.add((r, c))

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            visit.remove((r, c))
            cache[(r, c)] = res
            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                max_lip = max(max_lip, dfs(r, c, -1)) 

        return max_lip

        