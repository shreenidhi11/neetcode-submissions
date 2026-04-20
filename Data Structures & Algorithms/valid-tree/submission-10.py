class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {index: [] for index in range(n)}
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visit = set()
        path = set()


        def dfs(parent, node):
            if node in visit:
                return True

            if node in path:
                return False

            path.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if not dfs(node, nei):
                    return False
            path.remove(node)
            visit.add(node)
            return True



        return dfs(-1, 0) and len(visit) == n




