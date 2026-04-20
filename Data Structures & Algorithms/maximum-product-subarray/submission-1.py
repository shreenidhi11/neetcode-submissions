class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1,  1
        prod = 1

        for n in nums:
            tmp = n * curmax
            curmax = max(n * curmax, n * curmin, n)
            curmin = min(tmp, n * curmin, n)
            res = max(res, curmax)

        return res












