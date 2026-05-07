class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for index in range(1, len(prices)):
            profit = max(profit, prices[index] - buy)
            buy = min(prices[index], buy)
        
        return profit