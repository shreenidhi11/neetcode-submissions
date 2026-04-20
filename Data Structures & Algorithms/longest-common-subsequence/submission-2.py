class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def helper(i, j):
            if i == 0 and j == 0:
                if text1[i] == text2[j]:
                    return 1
                else:
                    return 0

            if i < 0 or j < 0:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            #match
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + helper(i - 1, j - 1)
            else:
                cache[(i, j)] = max(helper(i - 1, j), helper(i, j - 1))

            return cache[(i, j)]
        return helper(len(text1) - 1, len(text2) - 1)

            
            



        