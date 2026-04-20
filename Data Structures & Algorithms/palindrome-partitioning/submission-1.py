class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []


        def dfs(index, subres):
            if index >= len(s):
                result.append(subres.copy())
                return 

            for j in range(index, len(s)):
                if self.isPalindrome(s,index, j):
                    subres.append(s[index : j + 1])
                    dfs(j + 1, subres)
                    subres.pop()

            
        dfs(0,[])
        return result

    def isPalindrome(self, s,i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True



        