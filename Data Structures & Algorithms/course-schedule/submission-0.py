class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # define the preMap
        premap = {i:[] for i in range(numCourses)}

        # fill the values
        for i in range(len(prerequisites)):
            premap[prerequisites[i][0]].append(prerequisites[i][1])

        visit = set()
        # define your dfs function
        def dfs(crs):
            if crs in visit:
                return False

            if premap[crs] == []:
                return True

            visit.add(crs)
            # for loop for all the neighbouring nodes
            for pre in premap[crs]:
                if not dfs(pre): return False
            # you are done visiting the course
            visit.remove(crs)
            premap[crs] = []
            return True

        # now you will call this dfs function on all the nodes
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True







        