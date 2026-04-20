class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # using kadane's algorithm 
        res = nums[0]
        maxp, minp = 1, 1
        for num in nums:
            temp = num * maxp
            maxp = max(num * maxp, num, num * minp)
            minp = min(temp, num, num * minp)
            res= max(res, maxp)

        return res
        