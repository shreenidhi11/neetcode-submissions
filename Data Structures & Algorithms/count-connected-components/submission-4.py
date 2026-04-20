class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find_parent(self, child):
        while child != self.parent[child]:
            child = self.parent[child]
        return child

    def union(self, child1, child2):
        parent1, parent2 = self.find_parent(child1), self.find_parent(child2)
        if parent1 == parent2:
            return 0
        else:
            if self.rank[parent1] > self.rank[parent2]:
                self.rank[parent1] += self.rank[parent2]
                self.parent[parent2] = self.parent[parent1]
            else:
                self.rank[parent2] += self.rank[parent1]
                self.parent[parent1] = self.parent[parent2]

        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        total_components = 0

        for u, v in edges:
            total_components += dsu.union(u, v)
        
        return n - total_components



        