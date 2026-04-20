class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(index):
            if index < 0:
                return 0
            if index in cache:
                return cache[index]

            take = nums[index] + dfs(index - 2)
            dont_take = 0 + dfs(index - 1)
            cache[index] = max(take, dont_take)
            return cache[index]


        return dfs(len(nums) - 1)

        