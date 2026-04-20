class Solution:
    def checkValidString(self, s: str) -> bool:
        openmin, openmax = 0, 0

        for ch in s:
            if ch == "(":
                openmin += 1
                openmax += 1
            elif ch == ")":
                openmin-=1
                openmax-=1
            else:
                # this means the ch is *, which can be ( or )
                openmin-=1
                openmax+=1
            if openmax < 0:
                return False
            if openmin < 0:
                openmin = 0

        return openmin == 0
        