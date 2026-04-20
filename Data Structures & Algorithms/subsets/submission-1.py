class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
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
            helper(index + 1, subset)

        helper(0, [])
        return result


        