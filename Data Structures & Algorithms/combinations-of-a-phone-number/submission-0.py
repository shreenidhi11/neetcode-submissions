class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitchar = {'2': "abc", '3':"def",'4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9': "wxyz"}

        def dfs(curstr, i):
            if i >=len(digits):
                res.append(curstr)
                return

            for ch in digitchar[digits[i]]:
                dfs(curstr+ch,i+1)

        if digits:
            dfs("",0)
        return res
        