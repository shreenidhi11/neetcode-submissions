class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid1 = (top + bottom) // 2
            if target > matrix[mid1][-1]:
                top = mid1 + 1
            elif target < matrix[mid1][0]:
                bottom = mid1 - 1
            else:
                break

        if top > bottom:
            return False

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid2 = (l + r) // 2
            if matrix[mid1][mid2] == target:
                return True
            elif target > matrix[mid1][mid2]:
                l = mid2 + 1
            else:
                r = mid2 - 1

        return False

            
        