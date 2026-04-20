class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = nums[0]
        maxsum = nums[0]

        for i in range(1, len(nums)):
            if sum_ < 0:
                sum_ = 0
            sum_ = sum_ + nums[i]
            maxsum = max(sum_, maxsum)

        return maxsum
            


        