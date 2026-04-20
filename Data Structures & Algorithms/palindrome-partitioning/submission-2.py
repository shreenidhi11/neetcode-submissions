class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        result = []
        def check_palindrome(s):
            return s == s[::-1]

        def helper(index):
            if index >= len(s):
                result.append(res.copy())
                return

            for j in range(index, len(s)):
                if check_palindrome(s[index: j + 1]):
                    res.append(s[index: j + 1])
                    helper(j + 1)
                    res.pop()

        helper(0)
        return result
                    


                

        

        