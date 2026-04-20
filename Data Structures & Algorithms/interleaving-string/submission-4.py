class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # cache = {}
        # def helper(i, j, k):
        #     if k == len(s3):
        #         return i == len(s1) and j == len(s2)

        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     ans = False
        #     #match from s1
        #     if i < len(s1) and  s1[i] == s3[k]:
        #         ans |= helper(i + 1, j, k + 1)

        #     #match from s2
        #     if j < len(s2) and  s2[j] == s3[k]:
        #         ans |= helper(i, j + 1, k + 1)

        #     cache[(i, j)] = ans
        #     return cache[(i, j)]

        # return helper(0 , 0 , 0)

        # base case
        if len(s2) + len(s1) != len(s3):
            return False

        if not s2 and not s1 and s3:
            return False

        


        cache = [[ False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        cache[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i == len(s1) and j == len(s2):
                    continue

                ans = False
                #match from s1
                if i < len(s1) and  s1[i] == s3[i + j]:
                    ans |= cache[i + 1][j]

                #match from s2
                if j < len(s2) and  s2[j] == s3[i + j]:
                    ans |= cache[i][j + 1]

                cache[i][j] = ans

        return cache[0][0]






            



        