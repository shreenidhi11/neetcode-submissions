class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs(alice, index, M):
            if index == len(piles):
                return 0
            if (alice, index, M) in dp:
                return dp[(alice, index, M)]
            
            res = 0 if alice else float("inf")
            total = 0
            for X in range(1, 2 * M + 1):
                if index + X > len(piles):
                    break
                total += piles[index + X - 1]
                if alice:
                    res = max(res, total + dfs(not alice, index + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, index + X, max(M, X)))
            dp[(alice, index, M)] = res
            return res

        return dfs(True, 0, 1)
        


