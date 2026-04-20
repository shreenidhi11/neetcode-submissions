class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = defaultdict(int)
        for index, number in enumerate(nums):
            if target - number in sum_map:
                return [sum_map[target - number], index]
            else:
                sum_map[number] = index


        