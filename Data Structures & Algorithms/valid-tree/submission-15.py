class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # for a tree , there should be no cycle. so i need to run a dfs algorithm to check if there are cycle in the graph
        # and also check if all the nodes are visited
        visit = set()
        path = set()
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        def helper(node, parent):
            if node in visit:
                return True
            if node in path:
                return False
            path.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if not helper(nei, node):
                    return False
            visit.add(node)
            path.remove(node)
            return True

        return helper(0, -1) and len(visit) == n






        





        








