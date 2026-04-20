class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course -> prequisites
        # pre_map = {index:[] for index in range(numCourses)}
        # path, visit = set(), set()

        # for crs, pre in prerequisites:
        #     pre_map[crs].append(pre)

        # def findCycle(node):
        #     if node in path:
        #         return False
            
        #     if node in visit:
        #         return True

        #     path.add(node)
        #     for neighbours in pre_map[node]:
        #         if not findCycle(neighbours):
        #             return False

        #     visit.add(node)
        #     path.remove(node)
        #     return True

        # for node in range(numCourses):
        #     if not findCycle(node):
        #         return False

        
        # return True

        #tc and sc O(v + E)
        #using the kahn's algorithm, we start processing the courses that have no further dependincies
        indegree = {index: 0 for index in range(numCourses)}
        #this course has no dependedcy on anyh course to finish
        pre_map = {index:[] for index in range(numCourses)}

        for crs, pre in prerequisites:
            #course depends on the pre-map
            pre_map[pre].append(crs)
            indegree[crs] += 1

        queue = deque([index  for index, count in indegree.items() if count == 0])
        output = []
        while queue:
            current_course = queue.popleft()
            output.append(current_course)
            for nei in pre_map[current_course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return len(output) == numCourses
        

        




        