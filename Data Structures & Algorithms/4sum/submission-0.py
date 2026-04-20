class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                third = second + 1
                fourth = len(nums) - 1
                while third < fourth:
                    current_sum = nums[first] + nums[second] +  nums[third] + nums[fourth]

                    if current_sum == target:
                        result.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third += 1
                        fourth -= 1

                        #update to avoid the same values
                        while third < fourth and nums[third] == nums[third - 1]:
                            third += 1

                        while fourth > third and nums[fourth] == nums[fourth + 1]:
                            fourth -= 1

                    if current_sum > target:
                        fourth -= 1

                    if current_sum < target:
                        third += 1

        return result



                        



                


        