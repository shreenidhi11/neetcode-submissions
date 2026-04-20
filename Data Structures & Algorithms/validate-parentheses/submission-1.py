from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                st.append(s[i])
            else:
                if st:
                    if s[i] == ')':
                        if st[-1] != "(":
                            return False
                            
                    elif s[i] == '}':
                        if st[-1] != "{":
                            return False
                            

                    elif s[i] == ']':
                        print("Here")
                        if st[-1] != "[":
                            return False
                    st.pop()
                else:
                    return False
                        
        print(st)

        return True if not st else False



        