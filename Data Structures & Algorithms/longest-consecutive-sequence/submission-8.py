class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_length = 0

        for num in nums:
            if (num - 1) not in numset:
                cnt = 0
                while (num + cnt) in numset:
                    cnt += 1
                max_length = max(max_length, cnt)
        
        return max_length
                