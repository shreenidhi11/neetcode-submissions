"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        # q = deque()
        # q.append(root)

        # while q:
        #     n = len(q)
        #     for index in range(n):
        #         node = q.popleft()
        #         if index == n - 1:
        #             node.next = None
        #         else:
        #             node.next = q[0]
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        # return root
        depth_mp = {}
        def dfs(root, level):
            if not root:
                return root

            if level not in depth_mp:
                depth_mp[level] = root
            else:
                depth_mp[level].next = root
                depth_mp[level] = root

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return root
                

            


        