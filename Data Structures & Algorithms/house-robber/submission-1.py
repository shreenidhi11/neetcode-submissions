class Solution:
    def rob(self, nums: List[int]) -> int:
        [1,2,3,4,5]
        cache = {}
        def helper(index):
            if index == 0:
                return nums[0]
            if index < 0:
                return 0
            # base case
            if index in cache:
                return cache[(index)]

            option1 = nums[index] + helper(index - 2)
            option2 = 0 + helper(index - 1)
            cache[(index)] = max(option1, option2)
            return cache[(index)]

        return helper(len(nums) - 1)

        