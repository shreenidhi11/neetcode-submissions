class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites_map = {index:[] for index in range(numCourses)}
        output = []

        for a, b in prerequisites:
            prerequisites_map[a].append(b)
        
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
            output.append(node)
            path.remove(node)

            return True

        for num in range(numCourses):
            if not canFinish(num):
                return []

        return output