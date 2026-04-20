class Trie:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self,word):
        curr = self

        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.word = True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.addWord(w)

        ROWS,COLS=len(board),len(board[0])
        res,vis = set(), set()

        def dfs(r,c,node,word):
            # checking the boundary condition
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r,c) in vis  ):
                return
            vis.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]

            if node.word:
                res.add(word)
            
            # do the dfs in all 4 directions
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)

            vis.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(res)

        

















        