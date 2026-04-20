class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        res_set = set()
        i = 0


        for j in range(len(s)):
            while s[j] in res_set:
                res_set.remove(s[i])
                i+=1
            res_set.add(s[j])
            maxl = max(maxl, j-i+1)

        return maxl
            
        