class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board), len(board[0])

        # 1. dfs run to change the border 0 with x

        def dfs(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c]!="O":
                return
            board[r][c]= "T"
            # call the dfs in all 4 direction 
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # call the dfs
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and r in [0,rows-1] or c in [0, cols-1]:
                    dfs(r,c)


        # 2 Now all the not surrounding are converted to T, run a loop to covnert 
        # surround 0 to x
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] ="X"

        # run a loop to convert not surrounding to 0 again 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        





        