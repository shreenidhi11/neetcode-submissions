class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        res= []
        for src,dst in sorted(tickets)[::-1]:
            adj[src].append(dst)


        def dfs(node):
            while adj[node]:
                dst = adj[node].pop()
                dfs(dst)
            res.append(node)
        
        dfs("JFK")
        return res[::-1]










        