class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        grid_set = defaultdict(set)
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == ".":
                    continue
                else:
                    if grid[row][col] in row_set[row] or grid[row][col] in col_set[col] or grid[row][col] in grid_set[(row //3, col// 3)]:
                        return False
                    else:
                        row_set[row].add(grid[row][col])
                        col_set[col].add(grid[row][col])
                        grid_set[(row // 3, col // 3)].add( grid[row][col])
            
        return True	


        