class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # course -> prequisites
        pre_map = {index:[] for index in range(numCourses)}
        path, visit = set(), set()
        output = deque([])

        for crs, pre in prerequisites:
            pre_map[pre].append(crs)

        def findCycle(node):
            if node in path:
                return False
            
            if node in visit:
                return True

            path.add(node)
            for neighbours in pre_map[node]:
                if not findCycle(neighbours):
                    return False

            visit.add(node)
            output.appendleft(node)
            path.remove(node)
            return True

        for node in range(numCourses):
            if not findCycle(node):
                return []

        
        return list(output)
        