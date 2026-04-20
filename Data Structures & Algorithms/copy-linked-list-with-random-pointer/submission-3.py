"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        
        tmp = head

        # created the structure of individual nodes
        while tmp:
            old_to_new[tmp] = Node(tmp.val)
            tmp = tmp.next

        # now create 
        for node in old_to_new:
            if node.next:
                old_to_new[node].next = old_to_new[node.next]
            if node.random:
                old_to_new[node].random = old_to_new[node.random]

        return None if not  head   else old_to_new[head]

        

            
        