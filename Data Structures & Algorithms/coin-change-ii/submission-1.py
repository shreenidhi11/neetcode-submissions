class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def helper(index, target):
            # base case
            if index == 0:
                if target % coins[0] == 0:
                    return 1
                else:
                    return 0
            
            if (index, target) in cache:
                return cache[(index, target)]

            #dont take the coin
            not_take = helper(index - 1, target)
            # take the coin
            take_coin = 0
            if coins[index] <= target:
                take_coin =  helper(index, target - coins[index])
            
            cache[(index, target)] = not_take + take_coin
            return cache[(index, target)]
        return helper(len(coins) - 1, amount)
            
            


        