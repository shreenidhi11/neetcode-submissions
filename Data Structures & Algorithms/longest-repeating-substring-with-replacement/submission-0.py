class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # XYYX
        # AAABBCCD
        mydict = {}
        maxl = 0
        maxf = 0

        l, r = 0, 0
        while r< len(s):
            if s[r] not in mydict:
                mydict[s[r]] = 1
            else:
                mydict[s[r]]+=1
            maxf = max(maxf, mydict[s[r]])
            if (r-l+1) - maxf <= k:
                maxl = max(maxl, r-l+1 )
            else:
                # apply the slider logic
                mydict[s[l]]-=1
                l+=1
            r+=1

        return maxl
                








        