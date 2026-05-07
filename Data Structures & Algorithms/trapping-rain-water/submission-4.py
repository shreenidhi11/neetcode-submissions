class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for _ in range(len(height))]
        prefix[0] = height[0]
        suffix = [0 for _ in range(len(height))]
        suffix[-1] = height[-1]

        total_trapped = 0
        for index in range(1, len(height)):
            prefix[index] = max(prefix[index - 1], height[index])

        for index in range(len(height)-2, -1, -1):
            suffix[index] = max(suffix[index + 1], height[index])

        for index in range(len(height)):
            total_trapped += min(prefix[index], suffix[index]) - height[index]


        return total_trapped

