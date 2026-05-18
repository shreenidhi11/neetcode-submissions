class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        trapped = 0
        
        while l < r:
            if leftmax < rightmax:
                # move the left pointer inward to count trapped water
                l += 1
                # find whether the new height is smaller or greater so that water can trapped
                # if it is greater then a new leftmax is found for the next calculations
                # or else calculate the trapped water
                leftmax = max(leftmax, height[l])
                trapped += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                trapped += rightmax - height[r]

        return trapped





