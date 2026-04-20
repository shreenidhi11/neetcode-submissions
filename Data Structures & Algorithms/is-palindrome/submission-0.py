class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = s.replace(" ","").lower()
        news = [ch for ch in news if ch.isalnum()]

        return news == news[::-1]




        