class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = {len(s): 1}
        # for index in range(len(s) -1, -1, -1):
        #     if s[index] == "0":
        #         dp[index] = 0
        #     else:
        #         dp[index] = dp[index + 1]
            
        #     # now check if two digits character are possible
        #     if (index + 1) < len(s) and (s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456")):
        #         dp[index] += dp[index + 2]

        # return dp[0]

        # space optimized solution

        dp = {}
        dp[len(s)] = 1
        curr, prev = 1, -1


        # for index in range(len(s) - 1, -1, -1):
        #     if s[index] == "0":
        #         dp[index] = 0
        #     else:
        #         dp[index] = dp[index + 1]
            
        #     if index + 1 < len(s) and (s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456")):
        #         dp[index] += dp[index + 2]

        # return dp[0]
        
        for index in range(len(s) - 1, -1, -1):
            temp = 0
            if s[index] != "0":
                temp = curr
            
            if index + 1 < len(s) and (s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456")):
                temp += prev
            
            prev = curr
            curr = temp

        return curr










        