class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # basically this dp simply means starting from that character in the
        # string is there a word match in wordDict?
        dp = [False] * (len(s)+1)
        dp[len(s)] = True #base case

        # now iterate through every character in the string
        # neetcode
        for i in range(len(s)-1,-1,-1):
            # then check for everyword in the wordDict
            for word in wordDict:
                # check is our s has enough length to compare
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]










        