
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        path = set()
        visit = set()
        adj_list = {index: [] for index in range(n)}

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node):
            visit.add(node)
            for nei in adj_list[node]:
                if nei not in visit:
                    dfs(nei)
            
        total = 0

        for index in range(n):
            if index not in visit:
                dfs(index)
                total += 1

        return total




        