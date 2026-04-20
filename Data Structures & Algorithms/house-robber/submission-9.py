class Solution:
    def rob(self, nums: List[int]) -> int:
        # cache = {}
        # def helper(index):
        #     #base case
        #     if index == 0:
        #         return nums[index]

        #     if index < 0:
        #         return 0

        #     if index in cache:
        #         return cache[index]

        #     #option 1 - last idnex
        #     option1 = nums[index] + helper(index - 2)

        #     #option 2 - secondlast index
        #     option2 = 0 + helper(index - 1)

        #     cache[index] = max(option2, option1)
        #     return cache[index]

        # return helper(len(nums) - 1)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        cache = [0] * len(nums)
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for index in range(2, len(nums)):
            if index > 1:
                tmp = max(nums[index] + prev, 0 + curr)
                prev = curr
                curr = tmp

        return curr
            






        


    
        