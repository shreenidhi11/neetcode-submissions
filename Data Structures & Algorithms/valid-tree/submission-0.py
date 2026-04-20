class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        # created the adjacency list
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        # call the dfs
        def dfs(node, prev):
            if node in visit:
                return False
            
            # else
            visit.add(node)
            for pre in adj[node]:
                if pre == prev:
                    continue
                if not dfs(pre,node):
                    return False
            return True

        return dfs(0,-1) and n == len(visit)




        
        