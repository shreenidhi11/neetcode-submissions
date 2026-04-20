class Solution:
    def hammingWeight(self, n: int) -> int:
        # approach 1,counting all the bits and checking if 1 is there
        res = 0

        for i in range(32):
            res += (n >> i) & 1
        return res



        