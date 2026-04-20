class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # base case
        if len(s2) + len(s1) != len(s3):
            return False

        # we start from the bottom right and right side 
        # and go upwards
        dp = [[False] * (len(s1)+1) for str2 in range(len(s2)+1)]
        dp[len(s2)][len(s1)] = True

        # for loop
        for i in range(len(s2),-1,-1):
            for j in range(len(s1),-1,-1):
                if i < len(s2) and s2[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s1) and s1[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True

        return dp[0][0]


                


        