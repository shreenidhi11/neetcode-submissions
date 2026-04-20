class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
#         # uisng hashset and sorting the nums array
#         # naive way is to sort the nums first
#         nums.sort()
#         # create a hashset
#         nset = set(nums)

# #       iterate from 1 to len(nums) + 1
#         for index in range(len(nums) + 1):
#             if index + 1 not in nset:
#                 return index + 1
        
#         return -1
# Approach 2 using cyclic sort
# here we will check if the number is between 0 and <= nums.length + 1 and then we will check if it is in the correct postion
# if not then we will swap them

# then we will check if all the elements are placed in teir correct position
        index = 0
        while index < len(nums):
            # condition
            if 1 <= nums[index] <= len(nums) and nums[index] != nums[nums[index] - 1]:
                # find the correct position
                correct_position = nums[index] - 1
                # swap
                nums[index], nums[correct_position] =  nums[correct_position], nums[index]
            else:
                index += 1

        # at the end of this loop, you will get all the elements correctly placed in their position
        for index in range(len(nums)):
            if nums[index] != index + 1:
                return index + 1

        return len(nums) + 1











        