class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, index):
            # true base case
            if index == len(word):
                return True
            
            # error conditions
            if  r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or board[r][c] != word[index]:
                return False

            index += 1
            visit.add((r,c))
            res = dfs(r + 1, c, index) or dfs(r - 1, c, index) or dfs(r, c + 1, index) or dfs(r, c - 1, index)
            visit.remove((r,c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False




            

