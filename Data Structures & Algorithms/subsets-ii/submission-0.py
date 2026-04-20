class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #O(nlogn)
        subset = [] #O(n)
        result = []

        def helper(index, subset):
            # base case -> when index >= len(nums)
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            # two options
            # 1. take the element 
            subset.append(nums[index])
            helper(index + 1, subset)

            #2. do not take the element
            subset.pop()

            # avoid duplicate elements
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
                
            helper(index + 1, subset)

        helper(0, [])
        return result
        