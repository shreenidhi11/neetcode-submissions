class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def helper(index, target):
            if index == 0:
                if target % coins[index] == 0:
                    return target // coins[index]
                else:
                    return float("inf")

            if (index, target) in cache:
                return cache[(index, target)]

            not_take = 0 + helper(index - 1, target)
            take = float("inf")
            if coins[index] <= target:
                take = 1 + helper(index, target - coins[index])
            
            cache[(index, target)] = min(not_take, take)
            return cache[(index, target)]

        result = helper(len(coins) - 1, amount) 
        return -1 if result == float("inf") else result

        
            

            


        