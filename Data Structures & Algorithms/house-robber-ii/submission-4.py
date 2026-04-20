class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[0: -1]), self.helper(nums[1:]))
    
    def helper(self, nums):
        result = 0
        curr, prev = 0, 0
        index = 0
        while index < len(nums):
            result = max(prev + nums[index], curr)
            prev = curr
            curr = result
            index += 1



        return result 
