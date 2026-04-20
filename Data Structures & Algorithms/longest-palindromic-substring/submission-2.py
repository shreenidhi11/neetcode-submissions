class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromic_string = ""
        max_length = 0
        for index in range(len(s)):
            # even length
            l, r = index, index
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    max_length = r - l + 1
                    palindromic_string = s[l : r + 1]
                l -= 1
                r += 1


            # odd length
            l, r = index, index + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    max_length = r - l + 1
                    palindromic_string = s[l : r + 1]
                l -= 1
                r += 1

        return palindromic_string



            
            




        