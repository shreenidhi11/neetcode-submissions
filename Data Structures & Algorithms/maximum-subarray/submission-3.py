class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = nums[0]
        max_sum = nums[0]

        for index in range(1, len(nums)):
            if sum_ < 0:
                sum_ = 0
            sum_ += nums[index]
            max_sum = max(sum_, max_sum)
        
        return max_sum
        