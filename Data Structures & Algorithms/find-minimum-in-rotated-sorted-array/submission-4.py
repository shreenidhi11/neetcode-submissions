class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                min_num = min(min_num, nums[l])
                return min_num
            mid = (l + r )// 2
            min_num = min(min_num, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

            
        return min_num



