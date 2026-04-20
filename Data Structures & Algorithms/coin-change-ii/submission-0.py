class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins)+1) for i in range(amount+1)]
        # when you are at the 0th amount, there is 
        # only 1 way to reach that amount i.e no way (1)
        dp[0] = [1] * (len(coins)+1)

        # starting with next amount
        for a in range(1, amount+1):
            # trying all the coins
            for i in range(len(coins)-1,-1,-1):
                dp[a][i] = dp[a][i+1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]











        