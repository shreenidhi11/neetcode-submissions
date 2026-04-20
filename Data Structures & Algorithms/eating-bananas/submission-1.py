class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        res = 0
        while left <= right:
            mid = (left + right) // 2
            temp_h = 0
            for p in piles:
                temp_h += math.ceil(p / mid)
            if temp_h <= h:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res

        