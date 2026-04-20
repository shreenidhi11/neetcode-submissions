class Solution:
    def trap(self, height: List[int]) -> int:
        # l, r = 0, len(height) - 1
        # res = 0
        # leftmax, rightmax = height[l], height[r]

        # while l < r:
        #     if leftmax < rightmax:
        #         # start processing elements from the left side
        #         l += 1
        #         # also calculate the current leftmax in the fly
        #         leftmax = max(leftmax, height[l])
        #         res += (leftmax - height[l])
        #     else:
        #       # start processing elements from the right side
        #         r -= 1
        #         # also calculate the current rightmax in the fly
        #         rightmax = max(rightmax, height[r])
        #         res += (rightmax - height[r])

        # return res
        suffix = [-1] * len(height)
        suffix[-1] = height[-1]
        res = 0
        for index in range(len(height) - 2, -1, -1):
            suffix[index] = max(height[index], suffix[index + 1])
        leftmax = 0
        for index in range(len(height)):
            leftmax = max(leftmax, height[index])
            res += min(leftmax, suffix[index]) - height[index]

        return res









        

        


        