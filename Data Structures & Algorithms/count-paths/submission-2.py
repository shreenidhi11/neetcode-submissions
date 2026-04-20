class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def helper(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            up = helper(i - 1, j)
            left = helper(i , j - 1)
            cache[(i, j)] = up + left
            return cache[(i, j)]
        
        return helper(m - 1, n - 1)



        