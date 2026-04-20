class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        maping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9": "wxyz"
        }

        def dfs(i,word):
            if len(word) == len(digits):
                res.append(word)
                return

            for ch in maping[digits[i]]:
                dfs(i+1,word+ch)
            
        if digits:
            dfs(0,"")

        return res
            



                


            


    
        return res
            