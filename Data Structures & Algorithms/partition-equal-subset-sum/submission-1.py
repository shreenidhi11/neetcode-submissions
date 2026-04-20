class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half_total = total // 2
        if total % 2 == 1:
            return False

        dp = {}
        def helper(index, total):
            if total == 0:
                return True

            if index == 0:
                return nums[0] == total

            if (index, total) in dp:
                return dp[(index, total)]

            # dont pick a number
            not_pick = helper(index - 1, total)
            # pick a number
            pick = False
            if nums[index] <= total:
                pick =  helper(index - 1, total - nums[index])
            dp[(index, total)] = pick or not_pick

            return dp[(index, total)]

        return helper(len(nums) - 1, half_total)

        