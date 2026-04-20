class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_dict = {0 : 1}
        
        current_sum = 0
        subarray_cnt = 0

        for index in range(len(nums)):
            current_sum += nums[index]
            # if current_sum == k:
            #     subarray_cnt += 1
            if current_sum - k in sums_dict:
                subarray_cnt += sums_dict.get(current_sum - k, 0)
            # for future x - k sum storing along with count
            sums_dict[current_sum] = 1 + sums_dict.get(current_sum, 0)
        return subarray_cnt
            



