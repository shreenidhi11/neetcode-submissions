class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS =  len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        count = 0

        def helper(row, col):
            queue = deque()
            queue.append([row, col])
            visit.add((row, col))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or (nr, nc) in visit or grid[nr][nc] != "1":
                        continue
                    visit.add((nr, nc))
                    queue.append((nr, nc))


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visit:
                    helper(row, col)
                    count += 1

        return count

    
        



        