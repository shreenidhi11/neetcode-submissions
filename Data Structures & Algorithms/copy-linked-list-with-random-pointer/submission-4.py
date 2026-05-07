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
        old_to_new = defaultdict(Node)
        if not head:
            return head
        
        tmp = head

        while tmp:
            new_node = Node(tmp.val)
            old_to_new[tmp] = new_node
            tmp = tmp.next
        

        tmp = head
        while tmp:
            if tmp.next:
                old_to_new[tmp].next = old_to_new[tmp.next]
            if tmp.random:
                old_to_new[tmp].random = old_to_new[tmp.random]
            tmp = tmp.next

        return old_to_new[head]
