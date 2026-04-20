class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if  not n:
            return True

        # create a adjacency list
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        vis = set()

        def dfs(node,prev):
            if node in vis:
                return False

            vis.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei,node):
                    return False
            return True


        return dfs(0,-1) and n == len(vis)





        
        