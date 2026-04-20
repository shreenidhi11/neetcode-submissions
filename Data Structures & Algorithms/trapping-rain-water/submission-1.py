class Solution:
    def trap(self, height: List[int]) -> int:
        suffix_map = [0] * len(height)
        suffix_map[len(height) - 1] = height[-1]
        max_area = 0
        prefix = -1

        for index in range(len(height) - 2, -1, -1):
            suffix_map[index] = max(height[index], suffix_map[index + 1])


        for index in range(len(height)):
            prefix = max(prefix, height[index])
            max_area += min(suffix_map[index], prefix) - height[index]

        return max_area

        









        