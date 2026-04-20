class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def helper(i, j):
            # base condition
            if i == 0 and j == 0:
                return 1
            # boundary conidtion
            if i < 0 or j < 0:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            up = helper(i - 1, j)
            left = helper(i, j - 1)
            cache[(i, j)] = up + left
            return cache[(i, j)]

        return helper(m - 1, n - 1)
            # row = [1] * n

        # for i in range(m-1):
        #     newrow = [1] * n

        #     # calculate the values for this row
        #     for j in range(n-2,-1,-1):
        #         newrow[j] = newrow[j+1] + row[j]
        #     row = newrow

        # return row[0]

        