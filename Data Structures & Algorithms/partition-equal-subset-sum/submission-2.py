class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half_total = total // 2
        cache = {}
        def helper(index, current_total):
            if index == 0:
                if current_total - nums[index] == 0:
                    return True
                else:
                    return False

            if index < 0 or current_total < 0:
                return False
                
            if (index, current_total) in cache:
                return cache[(index, current_total)]
            
            not_take = helper(index - 1, current_total)
            take = False
            if nums[index] <= current_total:
                take = helper(index - 1, current_total - nums[index])
            cache[(index, current_total)] = take or not_take

            return cache[(index, current_total)]
        
        return helper(len(nums) - 1, half_total)
