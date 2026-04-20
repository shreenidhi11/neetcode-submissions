class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        # The adjacency list in this case will contain the edge and all the cost 
        # to other nodes
        edge = {i:[] for i in range(N)}  #list of cost, node

        # populate the edges with cost to other nodes
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edge[i].append([dist,j])
                edge[j].append([dist,i])

        # initialize the variables
        visit = set()
        minheap = [[0,0]] #cost,node
        mincost = 0

        while len(visit) < N:
            cost, node = heapq.heappop(minheap)
            if node in visit:
                continue
            mincost += cost
            visit.add(node)

            # explore the neighbours
            for costN, Node in edge[node]:
                if Node not in visit:
                    heapq.heappush(minheap,[costN,Node])
            
        return mincost









        

        

        








        