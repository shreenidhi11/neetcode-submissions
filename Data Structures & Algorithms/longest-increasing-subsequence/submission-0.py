class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # create a list to store the LIS for all the 
        # elements

        s = [1] * (len(nums)+1)

        for k in range(len(nums)):
            s[k] = 1
            for j in range(k):
                if nums[k] > nums[j] and s[j]+1 > s[k]:
                    s[k] = s[j] +1

        return max(s)

        