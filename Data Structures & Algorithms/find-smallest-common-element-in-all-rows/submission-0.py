class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # max count is m times, so maintain a hasmap of the number and count
        # then find the numbers with count equal to m
        # then return the smallest common number
        number_count_map = defaultdict(int)
        m, n = len(mat), len(mat[0])
        for row in range(m):
            for col in range(n):
                number_count_map[mat[row][col]] += 1

        number = float("inf")
        for num, cnt in number_count_map.items():
            if cnt == m:
                if number > num:
                    number = num
        return number





        