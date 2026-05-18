class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        trapped = 0
        
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                trapped += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                trapped += rightmax - height[r]

        return trapped





