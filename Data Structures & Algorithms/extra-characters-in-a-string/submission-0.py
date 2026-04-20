class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        wordset = set(dictionary)
        dp = {}

        def dfs(index):
            if index == n:
                return 0

            if index in dp:
                return dp[index]
            
            # option 1: treat current character as extra so count is 1
            res = 1 + dfs(index + 1)

            # option 2 : do not treat the current character as extra so find in the dictionary
            for j in range(index, n):
                if s[index: j + 1] in wordset:
                    res = min(res, dfs(j + 1))
            dp[index] = res
            return res

        return dfs(0)
        