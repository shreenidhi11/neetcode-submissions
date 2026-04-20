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
        mydict = {}

        tmp = head
        head2 = None
        tmp2 = None

        # create the deep copies first and store the index and node values
        while tmp:
            newnode = Node(tmp.val)
            if not head2:
                head2 = newnode
                tmp2 = newnode
            else:
                tmp2.next = newnode
                tmp2 = newnode
            mydict[tmp] = newnode
            tmp= tmp.next

        tmp = head
        tmp2 = head2

        # again iterate through the original linkedlist to locate the values
        # of random to correct nodes
        while tmp and tmp2:
            if tmp.random:
                 tmp2.random = mydict[tmp.random]
                
            tmp = tmp.next
            tmp2 = tmp2.next

        return head2
            
        








        






        