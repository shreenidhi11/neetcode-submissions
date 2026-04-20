class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create a prices list for all the nodes

        prices = [float("inf") for i in range(n)]

        # because you are starting with src mark the price as 0
        prices[src] = 0

        # there will be only k+1 loops
        for i in range(k+1):
            # create a temporary copy of prices
            tempP = prices.copy()
            
            for s,d,p in flights:
                if prices[s] == float("inf"):
                    continue
                
                if prices[s] + p < tempP[d]:
                    tempP[d] = prices[s] + p
            prices = tempP

        return -1 if prices[dst] == float("inf") else prices[dst]



        