class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # image a number line
        maxl = 1
        num = set(nums)

        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        # for i in range(len(nums)):
        #     if nums[i]-1 in num:
        #         incr = 0 
        #         while (nums[i]-1 + incr ) in num:
        #             incr+=1
        #         maxl = max(maxl,incr)
        # return maxl
        for i in range(len(nums)):
            if nums[i]-1 not in num:
                incr = 0 
                while (nums[i] + incr ) in num:
                    incr+=1
                maxl = max(maxl,incr)
        return maxl

            


        