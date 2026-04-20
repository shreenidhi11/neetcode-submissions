class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <=r :
            mid = (l + r) // 2
            # if found the target
            if nums[mid] == target:
                return True

            # check if we are in the left sorted portion of the array or the right sorted portion of the array
            if nums[l] < nums[mid]:
                # left sorted, check if the target can reside in this space i.e between left and mid
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1


            elif nums[l] > nums[mid]:
                # right sorted,  check if the target can reside in this space i.e between mid and right
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                
                else:
                    r = mid - 1

            else:
                # they are equal so we need to reduce the search space
                l += 1



        return False

        