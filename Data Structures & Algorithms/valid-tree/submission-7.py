class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edges_map = {index:[] for index in range(n)}

        for a, b in edges:
            edges_map[a].append(b)
            edges_map[b].append(a)


        for a, b in edges:
            edges_map[a].append(b)
        
        path = set()
        visit = set()

        def is_valid(node, prev):
            if node in visit:
                return True
            if node in path:
                return False

            path.add(node)
            for nei in edges_map[node]:
                if nei == prev:
                    continue
                if not is_valid(nei, node):
                    return False

            visit.add(node)
            # output.append(node)
            path.remove(node)
            return True

        # imagine you are running this for a tree, tree has a single root right
        # if we start this dfs from 0 then it will reach all the nodes and add itto visit
        # but other non reaching nodes will get left out in that case the len of visit wont equate to n
        return is_valid(0, -1) and len(visit) == n
