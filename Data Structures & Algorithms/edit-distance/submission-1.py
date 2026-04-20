class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def helper(i , j):
            # base case
            if i < 0:
                return j + 1

            if j < 0:
                #delete from i
                return i + 1
            if i < 0 and  j< 0:
                return 0
            
            if (i ,j) in cache:
                return cache[(i, j)]
            
            if word1[i] == word2[j]:
                cache[(i, j)] = helper(i - 1, j - 1)
            
            else:
                cache[(i , j)] = 1 + min(helper(i, j - 1), 
                                        helper(i - 1, j),
                                        helper(i - 1, j - 1))
            
            return cache[(i , j)] 
        return helper(len(word1) - 1, len(word2) - 1)


        