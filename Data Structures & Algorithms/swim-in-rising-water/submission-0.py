class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols = len(grid[0])
        visit = set((0,0))
        minheap = [[grid[0][0], 0,0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while minheap:
            t,r,c = heapq.heappop(minheap)

            if r == rows-1 and c == cols -1:
                return t

            for dr,dc in directions:
                nr , nc = r+dr, c+dc
                if nr == rows or nc == cols or nr < 0 or nc < 0 or (nr,nc) in visit:
                    continue
                visit.add((r,c))
                heapq.heappush(minheap, [max(t,grid[nr][nc]),nr,nc])

            



        