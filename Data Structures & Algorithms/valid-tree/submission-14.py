class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # for a tree , there should be no cycle. so i need to run a dfs algorithm to check if there are cycle in the graph
        # and also check if all the nodes are visited
        path = set()
        visit = set()
        adj_map = defaultdict(list)

        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
        
        def helper(node, parent):
            if node in visit:
                return True
            if node in path:
                return False
            path.add(node)
            for nei in adj_map[node]:
                if nei == parent:
                    continue
                if not helper(nei, node):
                    return False
            path.remove(node)
            visit.add(node)
            return True

        return helper(0, -1) and len(visit) == n



        





        








