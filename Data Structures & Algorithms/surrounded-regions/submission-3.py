class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        def dfs(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in visit or board[row][col] != "O":
                return
            board[row][col] = "T"
            visit.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        # turn the outer cells to T
        for rows in range(ROWS):
            for cols in range(COLS):
                if rows in [0, ROWS - 1] or cols in [0, COLS - 1]:
                    dfs(rows, cols)

        # turn the inner cells to X
        for rows in range(ROWS):
            for cols in range(COLS):
                if board[rows][cols] == "O":
                    board[rows][cols] = "X"


        # turn the outer cells to O
        for rows in range(ROWS):
            for cols in range(COLS):
                if board[rows][cols] == "T":
                    board[rows][cols] = "O"

            

    