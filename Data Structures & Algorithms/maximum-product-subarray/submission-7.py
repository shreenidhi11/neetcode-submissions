class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin, currmax = 1, 1
        res = nums[0]
        for n in nums:
            tmp = currmax * n
            currmax = max(n, currmax * n, currmin * n)
            currmin = min(n, tmp, currmin * n)
            res = max(currmax, res)

        return res


        