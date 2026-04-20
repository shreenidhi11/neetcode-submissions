class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def helper(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            # base case
            if (i, j) in cache:
                return cache[(i ,j)]
            if s[i] == t[j]:
                cache[(i, j)] = helper(i - 1, j) + helper(i - 1, j - 1)
            else:
                cache[(i ,j)] = helper(i - 1, j)
            return cache[(i ,j)]
        return helper(len(s) - 1, len(t) - 1)

        