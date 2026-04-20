class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero_cnt = 0
        l, r = 0, 0
        n = len(nums)
        max_length = 0

        if len(nums) == 1 and nums[0] == 0:
            return 1

        while r < n:
            if nums[r] == 0:
                zero_cnt += 1
                while zero_cnt > 1:
                    if nums[l] == 0:
                        zero_cnt -= 1
                    l += 1
                    
            max_length = max(max_length, r - l + 1)

            r += 1

        return max_length



        