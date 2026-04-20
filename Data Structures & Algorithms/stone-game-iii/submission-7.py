class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp = {}
        # def dfs(index):
        #     if index >= n:
        #         return 0
        #     if index in dp:
        #         return dp[index]
        #     res = float("-inf")
        #     total = 0
        #     for j in range(index, min(index + 3, n)):
        #         total += stoneValue[j]
        #         res = max(res, total - dfs(j + 1))

        #     dp[index] = res
        #     return res
        
        # result = dfs(0)
        # if result == 0:
        #     return "Tie"
        # elif result > 0:
        #     return "Alice"
        # else:
        #     return "Bob"


# tabulation method
        n = len(stoneValue)
        dp = [float("-inf")] * (n + 1)
        dp[n] = 0
        for index in range(n - 1, -1, -1):
            total = 0
            for j in range(index, min(index + 3, n)):
                total += stoneValue[j]
                dp[index] = max(dp[index], total - dp[j + 1])

        result = dp[0]
        if result == 0:
            return "Tie"
        elif result > 0:
            return "Alice"
        else:
            return "Bob"



        