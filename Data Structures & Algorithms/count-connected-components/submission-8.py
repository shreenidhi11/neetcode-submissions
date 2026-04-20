class DSU:
    def __init__(self, n):
        self.parent = [index for index in range(n)]
        self.rank = [1 for _ in range(n)]

    def findParent(self, child):
        if child != self.parent[child]:
            self.parent[child] = self.findParent(self.parent[child])
        return self.parent[child]


    def union(self, child1, child2):
        parent1, parent2 = self.findParent(child1), self.findParent(child2)
        if parent1 == parent2:
            return 0
        else:
            if self.rank[parent1] > self.rank[parent2]:
                self.rank[parent1] += self.rank[parent2]
                self.parent[parent2] = parent1
            else:
                self.rank[parent2] += self.rank[parent1]
                self.parent[parent1] = parent2
            return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        components = 0
        for u, v in edges:
            components += dsu.union(u, v)
        
        return n - components





        