class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]


    def findParent(self,child):
        while child != self.parent[child]:
            child = self.parent[child]
        return child

    def union(self,node1, node2):
        p1, p2 = self.findParent(node1), self.findParent(node2)
        if p1 == p2:
            return False
        else:
            if self.rank[p1] > self.rank[p2]:
                self.rank[p1] += self.rank[p2]
                self.parent[p2] = self.parent[p1]
            else:
                self.rank[p2] += self.rank[p1]
                self.parent[p1] = self.parent[p2]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)

        for a,b in edges:
            if not dsu.union(a, b):
                return [a,b]
        return []

        