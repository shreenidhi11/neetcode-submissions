class Solution:
    def rob(self, nums: List[int]) -> int:
        # cache = {}
        # def dfs(index):
        #     if index < 0:
        #         return 0
        #     if index in cache:
        #         return cache[index]

        #     take = nums[index] + dfs(index - 2)
        #     dont_take = 0 + dfs(index - 1)
        #     cache[index] = max(take, dont_take)
        #     return cache[index]


        def dfs(nums):

            # tabular approach
            if not nums:
                return 0

            if len(nums) == 1:
                return nums[0]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[1], nums[0])

            for index in range(2, len(nums)):
                dp[index] = max(nums[index] + dp[index - 2], 0 + dp[index - 1])
            
            return dp[-1]

        return max(dfs(nums[1:]), dfs(nums[0: -1]), nums[0])

        


        