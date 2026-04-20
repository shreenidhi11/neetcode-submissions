class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #in a valid tree there cannot be loops
        #Also a graph can be disconnected which means i need to cover all the points to check if its a tree
        visit = set()
        path = set()
        edges_map = defaultdict(list)

        for u, v in edges:
            edges_map[u].append(v)
            edges_map[v].append(u)

        def helper(parent, node):
            if node in path:
                return False
            if node in visit:
                return True
            path.add(node)
            for nodes in edges_map[node]:
                if nodes == parent:
                    continue
                elif not helper(node, nodes):
                    return False
            visit.add(node)
            path.remove(node)
            return True


        return helper(-1, 0) and len(visit) == n
        #O(V + E)
        #O(V + E)




            
