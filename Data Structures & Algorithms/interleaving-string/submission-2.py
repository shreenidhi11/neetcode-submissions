class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        def helper(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if (i, j) in cache:
                return cache[(i, j)]

            ans = False
            #match from s1
            if i < len(s1) and  s1[i] == s3[k]:
                ans |= helper(i + 1, j, k + 1)

            #match from s2
            if j < len(s2) and  s2[j] == s3[k]:
                ans |= helper(i, j + 1, k + 1)

            cache[(i, j)] = ans
            return cache[(i, j)]

        return helper(0 , 0 , 0)

            



        