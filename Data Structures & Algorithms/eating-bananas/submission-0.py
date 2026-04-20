class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        t = 0
        ans = float('inf')

        while l <=r:
            mid = (l+r)//2
            t = self.calctime(piles, mid)
            if t <= h:
                ans = mid
                r = mid-1
            else:
                l = mid+1
            
        
        # return rangebs[mid]
        return ans

    def calctime(self,piles, value):
        time = 0
        for i in piles:
            time += (i + value - 1) // value
        return time






        