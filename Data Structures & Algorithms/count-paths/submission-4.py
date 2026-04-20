class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache = {}
        # def helper(i, j):
        #     #base case
        #     if i == 0 and j == 0:
        #         return 1

        #     if i < 0 or j < 0:
        #         return 0

        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     #option1
        #     up = helper(i - 1, j)
        #     #option 2
        #     left = helper(i, j - 1)
        #     cache[(i, j)] = up + left
        #     return cache[(i, j)]

        # return helper(m - 1, n - 1)


        cache = [[ 0 for _ in range((n))] for _ in range((m))]
        #base case
        for col in range((n)):
            cache[0][col] = 1
        

        for row in range((m)):
            cache[row][0] = 1


        for i in range(1, m):
            for j in range(1, n):
                up = cache[i - 1][j]
                left = cache[i][j - 1]
                cache[i][j] = up + left

        return cache[m - 1][n - 1]

        