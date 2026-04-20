class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res= []

        def balanced(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                balanced(opened+1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                balanced(opened, closed+1)
                stack.pop()

        
        balanced(0, 0)
        return res



        