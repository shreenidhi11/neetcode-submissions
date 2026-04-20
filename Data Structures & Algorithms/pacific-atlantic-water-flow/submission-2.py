class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl = set()
        pac = set()
        res = []

        def dfs(r,c,result,value):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in result or heights[r][c] < value:
                return

            result.add((r,c))
            dfs(r+1, c, result, heights[r][c]) 
            dfs(r-1, c, result, heights[r][c])
            dfs(r, c-1, result, heights[r][c])
            dfs(r, c+1, result, heights[r][c])

        # we know cells from top and left will flow to pacific
        # r = 0, ROWS-1
        for c in range(COLS):
            dfs(0,c,pac, heights[0][c])
            dfs(ROWS-1,c, atl, heights[ROWS-1][c])

        # we know cells from bottom and right will flow to atlantic
        # c = 0,COLS-1
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1, atl, heights[r][COLS-1])


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res



