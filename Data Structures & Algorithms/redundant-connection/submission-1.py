class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1 for _ in range(len(edges)+1)]

        def find(node):
            while node != parent[node]:
                node = parent[node]
            
            return node

        def union(u,v):
            p1, p2 = find(u), find(v)
            if p1 == p2:
                return False
            else:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p1]+=rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2]+=rank[p1]
            return True


        res = 0
        for u,v in edges:
            if not union(u,v):
                return [u,v]






        
        