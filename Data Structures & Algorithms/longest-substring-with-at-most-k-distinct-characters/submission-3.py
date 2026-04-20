class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_count = {}
        max_length = 0
        l, r = 0, 0
        n = len(s)
        while r < n:
            if s[r] not in char_count:
                char_count[s[r]] = 0
            char_count[s[r]] += 1

            # while the window is still invalid keep on shifting the left pointer
            while len(char_count) > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1
            
            # window is already valid, count the max_length
            max_length = max(max_length, r - l + 1)
            r += 1
        
        return max_length

        # tc is O(N)
        # sc is O(m) where m is unique characters 


              