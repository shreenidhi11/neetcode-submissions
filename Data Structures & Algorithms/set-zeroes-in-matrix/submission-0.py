class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # let us find the rows and coloumns having zeroes
        zeroset = []

        def setZero(zeroset):
            for r,c in zeroset:
                # suppose[1,1]
            # consider the rows
                matrix[r] = [0 for col in range(len(matrix[0]))]
            # consider the columns
                for row in range(len(matrix)):
                    matrix[row][c] = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeroset.append([row,col])

        setZero(zeroset)

        


        
        