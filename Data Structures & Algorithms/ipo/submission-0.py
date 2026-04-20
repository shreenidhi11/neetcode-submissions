class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxprofit = [] #profits to consider
        mincap_profit = [(c, p) for c, p in zip(capital, profits)] # minimum capacity projects based on available funding (w)
        heapq.heapify(mincap_profit)

        for _ in range(k):
            while mincap_profit and mincap_profit[0][0] <= w:
                c, p = heapq.heappop(mincap_profit)
                heapq.heappush(maxprofit, -1 * p)
            
            if not maxprofit:
                break
            w += -1 * heapq.heappop(maxprofit)
        
        return w



        