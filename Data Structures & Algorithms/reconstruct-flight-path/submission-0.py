class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort the tickets to get the path in lexicographical manner
        tickets.sort()
        # initialize the adjacency list
        adj = {src:[] for src,dst in tickets}


        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"] #always start from jfk

        def dfs(src):
            if len(res) == len(tickets) +1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            # iterate through all the nodes in the adj for the current src
            for index , v in enumerate(temp):
                adj[src].pop(index)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(index, v)
                # pop because we are removing from the end
                res.pop()
            return False

        dfs("JFK")
        return res







        