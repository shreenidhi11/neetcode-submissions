class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1] * n
        # we go from left to right and comapre if left rating is smaller than the right rating
        # then loop from right to left and compare if the left rating is greater than the right rating

        # left to right
        for index in range(1, n):
            if ratings[index] > ratings[index - 1]:
                result[index] = result[index - 1] + 1

        # right to left
        for index in range(n - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                # we use max here because we do not want to ignore the already high value set from the previous pass
                result[index] = max(result[index + 1] + 1, result[index])

        return sum(result)