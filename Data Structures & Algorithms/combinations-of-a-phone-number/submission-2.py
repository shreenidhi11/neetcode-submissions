class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        res= []

        if not digits:
            return res

        def dfs(index, word):
            # base condition
            if len(word) == len(digits):
                res.append(word)
                return

            for ch in maping[digits[index]]:
                dfs(index + 1, word + ch)

        dfs(0, "")
        return res
            

                