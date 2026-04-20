class Solution:
    def jump(self, nums: List[int]) -> int:
        # using 1d bfs
        l, r= 0, 0
        res = 0
        while r < len(nums) - 1:
            farthest = 0
            for index in range(l, r + 1):
                farthest = max(farthest, index + nums[index])
            
            l = r + 1
            r = farthest
            res += 1
        return res