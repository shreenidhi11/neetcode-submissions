class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        root = self
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        output = set()

        root = TrieNode()
        # added all the words
        for word in words:
            root.addWord(word)


        def dfs(r, c, root, word):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or board[r][c] not in root.children:
                return
            visit.add((r, c))
            root = root.children[board[r][c]]
            word += board[r][c]
            if root.end:
                output.add(word)


            dfs(r + 1, c, root, word)
            dfs(r - 1, c, root, word)
            dfs(r, c + 1, root, word)
            dfs(r, c - 1, root, word)
            visit.remove((r,c))


        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(output)

                

        






        