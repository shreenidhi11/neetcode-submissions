class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}
        for index in range(len(s) - 1, - 1, - 1):
            if s[index] == "0":
                cache[(index)] = 0
            else:
                cache[(index)] = cache[(index + 1)]

            if (index + 1 < len(s)) and(s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456")):
                cache[(index)] += cache[(index + 2)]

        return cache[0]



        