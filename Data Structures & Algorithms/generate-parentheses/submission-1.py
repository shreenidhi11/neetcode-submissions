class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res =[]
        def dfs(opened, close):
            if opened == close == n:
                res.append("".join(stack))
                return
            
            if opened < n:
                stack.append("(")
                dfs(opened + 1, close)
                stack.pop()
            
            if close < opened:
                stack.append(")")
                dfs(opened, close + 1)
                stack.pop()

        dfs(0, 0)
        return res



        