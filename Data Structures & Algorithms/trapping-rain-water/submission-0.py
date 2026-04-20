class Solution:
    def trap(self, height: List[int]) -> int:
            # find the prefixMax
            prefixMax = [ 0 for i in height]
            prefixMax[0] = height[0]

            for i in range(1,len(height)):
                prefixMax[i] = max(prefixMax[i-1], height[i])

            # find the suffixMax
            suffixMax = [ 0 for i in height]
            suffixMax[-1] = height[-1]

            for i in range(len(height)-2,-1,-1):
                suffixMax[i] = max(suffixMax[i+1], height[i])

            cnt = 0

            for i in range(len(height)):
                if height[i] < prefixMax[i] and height[i] < suffixMax[i]:
                    cnt+= min(prefixMax[i], suffixMax[i]) - height[i]

            return cnt
        