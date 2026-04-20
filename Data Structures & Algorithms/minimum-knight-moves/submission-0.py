class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[-2, 1], [-2, -1],[-1, 2], [-1, -2],[1, 2],[1, -2],[2, 1], [2, -1]]
        q = deque([(0, 0)])
        visit = set()
        step = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == x and c == y:
                    return step

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr, nc) in visit:
                        continue
                    q.append([nr, nc])
                    visit.add((nr, nc))
            step += 1

        return step

            


        
        