class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        sequence_length = 0

        for num in nums:
            if (num - 1) not in num_set:
                count = 0
                while (num + count) in num_set:
                    count += 1
                sequence_length = max(sequence_length, count)
        
        return sequence_length