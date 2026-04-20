class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix)
        left,right = 0, len(matrix[0])

        while left < right and top < bottom:
            # left to right, increment top for next iteration
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1

            # Now go from top to bottom, decrement your right for next iteration
            for j in range(top,bottom):
                res.append(matrix[j][right-1])
            right-=1

            if not (left < right and top < bottom):
                break

            # Now go from right to left, decrement bottom for next iteration
            for k in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][k])
            bottom-=1

            # Now go from bottom to up, increment left for next iteration
            for b in range(bottom-1, top-1, -1):
                res.append(matrix[b][left])
            left+=1

        return res



