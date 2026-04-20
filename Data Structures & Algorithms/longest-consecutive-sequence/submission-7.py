class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in num_set:
                length = 0
                while (length + num) in num_set:
                    length += 1
                max_len = max(length, max_len)
        return max_len




                