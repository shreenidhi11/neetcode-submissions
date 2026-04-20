class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # using DFS to find a cycle
        # a -> b
        # b(depending) -> a(dependent)
        
        prerequisites_map = {index:[] for index in range(numCourses)}

        for a, b in prerequisites:
            prerequisites_map[b].append(a)
        
        path = set()
        visit = set()

        def canFinish(node):
            if node in visit:
                return True
            if node in path:
                return False

            path.add(node)
            for nei in prerequisites_map[node]:
                if not canFinish(nei):
                    return False

            visit.add(node)
            path.remove(node)

            return True

        for num in range(numCourses):
            if not canFinish(num):
                return False

        return True


        