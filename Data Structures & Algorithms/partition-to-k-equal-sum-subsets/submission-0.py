class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        subset_sum = sum(nums) / k
        nums.sort(reverse=True)
        used = [False] * len(nums)
        def backtrack(index, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == subset_sum:
                return backtrack(0, k - 1, 0)
            
            for j in range(index, len(nums)):
                if used[j] or nums[j] + subsetSum > subset_sum:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False

            return False

        return backtrack(0, k, 0)