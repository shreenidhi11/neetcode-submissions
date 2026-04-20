class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        max_sum = nums[0]

        for index in range(len(nums)):
            if sum_ < 0:
                sum_ = 0
            
            sum_ += nums[index]
            max_sum = max(max_sum, sum_)
        
        return max_sum

        