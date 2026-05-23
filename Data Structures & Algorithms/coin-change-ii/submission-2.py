class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def helper(index, current_amount):
            if index == 0:
                if current_amount % coins[index] == 0:
                    return 1
                else:
                    return 0

            if index < 0 or current_amount > amount:
                return 0

            if (index, current_amount) in cache:
                return cache[(index, current_amount)]
            
            dont_take = helper(index - 1, current_amount)
            take = 0
            if coins[index] <= current_amount:
                take = helper(index, current_amount - coins[index])
            cache[(index, current_amount)] = dont_take + take
            return cache[(index, current_amount)]
        
        return helper(len(coins) - 1, amount)