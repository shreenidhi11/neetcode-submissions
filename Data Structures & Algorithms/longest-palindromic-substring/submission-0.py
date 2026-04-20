class Solution:
    def longestPalindrome(self, s: str) -> str:

        reslen = 0
        resinx = 0

        # odd length

        for i in range(len(s)):
            l,r = i,i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    resinx = l
                    reslen =  (r-l+1)
                
                l -= 1
                r += 1

            # even length
            l,r = i,i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    resinx = l
                    reslen =  r-l+1
                
                l -=1
                r+=1

        return s[resinx: resinx + reslen]

        



        