class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            if len(nums) == 0:
                return 0

            if len(nums) == 1:
                return nums[0]


            cache = [0] * len(nums)
            prev = nums[0]
            curr = max(nums[0], nums[1])

            for index in range(2, len(nums)):
                tmp = max(curr, nums[index] + prev)
                prev = curr
                curr = tmp

            return curr
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[0: -1]), helper(nums[1:]))
    

