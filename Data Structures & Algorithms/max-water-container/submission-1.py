class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i,j = 0,len(heights)-1

        while i <=j:
            h = min(heights[i],heights[j])
            w = abs(j-i)
            area = h * w
            max_water = max(area, max_water)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1

        return max_water






        