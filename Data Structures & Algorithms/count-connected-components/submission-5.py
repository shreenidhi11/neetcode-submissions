class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def findParent(self, child):
        while child != self.parent[child]:
            child = self.parent[child]

        return child

    def union(self, child1, child2):
        parent1, parent2 = self.findParent(child1), self.findParent(child2)
        if parent1 == parent2:
            return False
        else:
            if self.rank[parent1] > self.rank[parent2]:
                self.rank[parent1] += self.rank[parent2]
                self.parent[parent2] = self.parent[parent1]
            else:
                self.rank[parent2] += self.rank[parent1]
                self.parent[parent1] = self.parent[parent2]
        return True




class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        total = 0
        for a, b in edges:
            n -= dsu.union(a, b)
            # total += dsu.union(a, b)
            
        return n
        # return n - total



        