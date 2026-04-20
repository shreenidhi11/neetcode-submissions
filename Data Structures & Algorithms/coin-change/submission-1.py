class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def helper(index, target):
            #base case
            if index == 0:
                if target % coins[index] == 0:
                    return target // coins[0]
                else:
                    return float("inf")

            if index < 0:
                return float("inf")

            if (index, target) in cache:
                return cache[(index, target)]
            
            not_pick = 0 + helper(index - 1, target)
            pick = float("inf")
            if coins[index] <= target:
                pick = 1 + helper(index, target - coins[index])
            cache[index, target] = min(pick, not_pick)
            return cache[(index, target)]

        total_coins = helper(len(coins) - 1, amount)

        return -1 if total_coins == float("inf") else total_coins
        
            




