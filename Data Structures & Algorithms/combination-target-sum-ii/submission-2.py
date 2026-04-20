class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []

        def helper(index, subset, amount):
            if target == amount:
                result.append(subset.copy())
                return

            if index >= len(nums) or target < amount:
                return 


            subset.append(nums[index])
            helper(index + 1, subset, amount + nums[index])

            subset.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            helper(index + 1, subset, amount)


        helper(0, [], 0)
        return result

    #time complexity is O(2 )
        