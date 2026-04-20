class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #using hamiltonion concept, like travelling all the nodes
        #first I will visit all the lexicogrpa add it in result and then reverse it and return the result

        #first build the connections in reverse order
        adj_list = defaultdict(list)
        result = []

        for src, dst in sorted(tickets)[:: -1]:
            adj_list[src].append(dst)


        def helper(src):
            while adj_list[src]:
                next_dst = adj_list[src].pop()
                helper(next_dst)
            result.append(src)
        

        helper("JFK")
        return result[::-1]
            
            




        