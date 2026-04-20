class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = [1] * len(nums)

        for index in range(len(nums)):
            current_num = nums[index]
            for j in range(index):
                if current_num > nums[j] and sequence[j] + 1 > sequence[index]:
                    sequence[index] = sequence[j] + 1

        return max(sequence) 
        
        