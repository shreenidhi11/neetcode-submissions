class Solution:
    def arrangeCoins(self, n: int) -> int:
        total_complete_rows = 0
        current_row = 1
        while n > 0:
            n = n - current_row
            if n < 0:
                return total_complete_rows
            current_row += 1
            total_complete_rows += 1

        return total_complete_rows
        



        