class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # initialize the 2DP.

        dp = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]

        # Now fill in the basecase
        # fill in the last column, this means only row changes
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i

        # fill in the last row, this means only col changes
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j


        # now start filling the dp table in the bottom up approach
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1],  dp[i+1][j],  dp[i][j+1])

        return dp[0][0]


        
