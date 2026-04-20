class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while node!=parent[node]:
                node = parent[node]
            
            return node

        def union(u,v):
            p1, p2 = find(u), find(v)
            if p1 == p2:
                return 0
            else:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p1]+=rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2]+=rank[p1]
            return 1


        res = 0
        for u,v in edges:
            res+=union(u,v)

        return n - res





        