class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        prod = 1
        for index, val in enumerate(nums):
            result[index] = prod
            prod *= val

        prod = 1

        for index in range(len(nums) - 1, -1, -1):
            result[index] *= prod
            prod *= nums[index]

        return result

        


        