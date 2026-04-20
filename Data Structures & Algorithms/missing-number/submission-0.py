class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(range(0,len(nums)+1)))
        