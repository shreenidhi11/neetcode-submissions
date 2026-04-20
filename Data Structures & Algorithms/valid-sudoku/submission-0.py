class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        cell = defaultdict(set)
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowset[r] or board[r][c] in colset[c] or board[r][c] in cell[(r // 3, c // 3)]:
                    return False
                rowset[r].add(board[r][c])
                colset[c].add(board[r][c])
                cell[(r // 3, c // 3)].add(board[r][c])

        return True



        