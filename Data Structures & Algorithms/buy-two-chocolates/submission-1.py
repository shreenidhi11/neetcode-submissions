class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        min_left_over = float("inf")
        min_sum = float("inf")

        if prices[0] + prices[1] > money:
            return money

# This is not needed, if we want to minimize the sum then we will obviosuly select the first two elements
        for index in range(len(prices) - 1):
            curr_sum = prices[index] + prices[index + 1]
            if money - curr_sum < 0:
                break
            elif min_sum > curr_sum:
                min_sum = curr_sum
                min_left_over = money - curr_sum

        return min_left_over



        