class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s and t:
            return ""
        
        if len(s) < len(t):
            return ""

        if len(s) == 1 and len(t) == 1:
            if s[0] == t[0]:
                return s[0]
            else:
                return ""

        thash = {}
        maxL = float('inf') 
        
        # this will prepare a hashmap with all the characters in t
        for ch in t:
            if ch not in thash:
                thash[ch] = 1
            else:
                thash[ch] +=1
        # print(thash)

        # Now store the count of chars in t
        t_len = len(t)
        cnt = 0
        s_index = -1

        # initialize l,r
        l,r = 0,0

        while r < len(s):
            if s[r] not in thash:
                thash[s[r]] = -1
            else:
                if thash[s[r]] > 0:
                    cnt+=1
                thash[s[r]] -= 1

            # print(cnt, thash)
            while cnt == t_len:
                if r-l+1 < maxL:
                    maxL = r-l+1
                    s_index = l
                # Now try to resize the window
                # print(s[l:r+1])
                thash[s[l]] += 1
                if thash[s[l]] > 0:
                    cnt-=1
                l+=1 
            r+=1

        return "" if s_index == -1 else s[s_index:s_index + maxL]
            