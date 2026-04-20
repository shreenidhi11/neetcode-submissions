class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # define teh premap
        premap = {crs:[] for crs in range(numCourses)}

        # fill the premap
        for crs , pre in prerequisites:
            premap[crs].append(pre)

        # define two sets
        visit, cycle  = set(), set()

        # define the output
        output = []

        # define the dfs
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            # else

            cycle.add(crs)
            for pre in premap[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)


        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return output





        