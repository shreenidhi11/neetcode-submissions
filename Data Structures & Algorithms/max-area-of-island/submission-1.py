class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0],[1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()
        max_area = 0

        def bfs(r, c):
            visit.add((r, c))
            q.append((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = dr + row, dc + col
                    if newRow < 0 or newRow == ROWS or newCol < 0 or newCol == COLS or (newRow, newCol) in visit or grid[newRow][newCol] != 1:
                        continue
                    visit.add((newRow, newCol))
                    q.append((newRow, newCol))
                    area += 1

            return area



        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
                    

        return max_area

        #Time complexity - O(m * n)
        #Space complexity - O(m * n)

        
        