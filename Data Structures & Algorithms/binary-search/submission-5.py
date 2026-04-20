class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1

        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l +r) // 2
            if nums[mid] == target:
                res= mid
                return res
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res



        