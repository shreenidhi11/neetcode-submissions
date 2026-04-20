class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # here we use a normal kadane algorithm but with a twist. 
        # we maintain max and min number. using kadane we get the max sum subarray. then to consider the wrap around we 
        # we do total sum - min and return the max(max, total sum - min)
        currmin, currmax = 0, 0
        total = 0
        globalmin, globalmax = nums[0], nums[0]
        for num in nums:
            currmax = max(currmax + num, num)
            currmin = min(currmin + num, num)
            total += num

            globalmax = max(globalmax, currmax)
            globalmin = min(globalmin, currmin)
        
        if globalmax < 0:
            # this means the entire array has negative elements
            return globalmax

        return max(globalmax, total - globalmin)




        