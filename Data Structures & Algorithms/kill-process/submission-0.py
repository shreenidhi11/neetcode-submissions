class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        result = []
        parent_child_map = {id:[] for id in ppid}
        for index in range(len(ppid)):
            parent_child_map[ppid[index]].append(pid[index])
        def dfs(node):
            if node not in parent_child_map:
                result.append(node)
                return 
            for children in parent_child_map[node]:
                dfs(children)
            result.append(node)
        
        dfs(kill)
        
        return result




        