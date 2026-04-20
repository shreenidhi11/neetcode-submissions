class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def helper(index, total):
            if index < 0:
                if total == target:
                    return 1
                else:
                    return 0

            #if index == 0:
            if (index, total) in cache:
                return cache[(index, total)]

            positive = helper(index - 1, total + nums[index])
            negative = helper(index - 1, total - nums[index])
            cache[(index, total)] = positive + negative
            return cache[(index, total)]

        return helper(len(nums) - 1, 0)
            





        