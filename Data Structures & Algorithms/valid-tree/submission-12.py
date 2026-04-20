class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {index: [] for index in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visit = set()
        path = set()
        def dfs(node, parent):
            if node in visit:
                return True
            if node in path:
                return False
            path.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            visit.add(node)
            path.remove(node)
            return True
        
        return dfs(0, -1) and len(visit) == n
        
            
