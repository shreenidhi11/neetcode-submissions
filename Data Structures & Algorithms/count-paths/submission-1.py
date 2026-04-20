class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache = {}
        # def helper(i, j):
        #     # base condition
        #     if i == 0 and j == 0:
        #         return 1
        #     # boundary conidtion
        #     if i < 0 or j < 0:
        #         return 0
        #     if (i, j) in cache:
        #         return cache[(i, j)]
        #     up = helper(i - 1, j)
        #     left = helper(i, j - 1)
        #     cache[(i, j)] = up + left
        #     return cache[(i, j)]

        # return helper(m - 1, n - 1)


        cache = [[0 for j in range(n)]for i in range(m)]
        
        for r in range(m):
            cache[r][0] = 1
        
        for c in range(n):
            cache[0][c] = 1

        for i in range(1, m):
            for j in range(1, n):
                up = cache[i - 1][j]
                left = cache[i][j - 1]
                cache[i][j] = up + left

        return cache[m - 1][n - 1]
                

        

        