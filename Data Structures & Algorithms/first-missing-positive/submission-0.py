class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # uisng hashset and sorting the nums array
        nums.sort()

        nset = set(nums)

        for index in range(len(nums) + 1):
            if index + 1 not in nset:
                return index + 1
        
        return -1

        