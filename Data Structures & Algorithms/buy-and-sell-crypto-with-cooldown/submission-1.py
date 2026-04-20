class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def helper(index, buy):
            if index >= len(prices):
                return 0

            if (index, buy) in dp:
                return dp[(index, buy)]

            if buy:
               dp[(index, buy)] = max( - prices[index] + helper(index + 1, 0), 0 + helper(index + 1, 1))
            else:
                dp[(index, buy)] = max( prices[index] + helper(index + 2, 1), 0 + helper(index + 1, 0))
            return dp[(index, buy)]

        return helper(0, 1)



        