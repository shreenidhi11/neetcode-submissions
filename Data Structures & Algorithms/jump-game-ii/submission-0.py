class Solution:
    def jump(self, nums: List[int]) -> int:
        # using bfs in 1d
        res = 0
        l,r = 0,0

        # here l and r are boundaries of your levels

        while r < len(nums)-1:
            farthest = 0

            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])

            l = r+1
            r = farthest

            res+=1

        return res

        



        