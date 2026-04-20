class Solution:
    def rob(self, nums: List[int]) -> int:
        cache1 = {}
        cache2 = {}
        def helper(index, flag):
            if flag:
                if index == 0:
                    return nums[0]
                if index < 0:
                    return 0
            else:
                if index == len(nums) - 1:
                    return nums[-1]
                elif index >= len(nums):
                    return 0

            # base case
            if flag:
                if index in cache1:
                    return cache1[(index)]
            else:
                if index in cache2:
                    return cache2[(index)]
            if flag:
                option1 = nums[index] + helper(index - 2,flag)
                option2 = 0 + helper(index - 1, flag)
                cache1[(index)] = max(option1, option2)
                return cache1[(index)]
            else:
                option1 = nums[index] + helper(index + 2, flag)
                option2 = 0 + helper(index + 1, flag)
                cache2[(index)] = max(option1, option2)
                return cache2[(index)]


        amount = helper(len(nums) - 2, True)
        amount = max(amount, helper(1, False))
        return max(amount, nums[0])

        