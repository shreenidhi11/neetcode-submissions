class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def helper(index, buy):
            if index >= len(prices):
                return 0
            if (index, buy) in cache:
                return cache[(index, buy)]

            if buy:
                cache[(index, buy)] = max(-prices[index] + helper(index + 1, 0), 0 + helper(index + 1, 1))
                # buying now
                
            else:
                cache[(index, buy)] = max(prices[index] + helper(index + 2, 1), 0 + helper(index + 1, 0))
            return cache[(index, buy)]

        return helper(0,1)



            


        