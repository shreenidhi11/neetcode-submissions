# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1,2,3,4
        # listnodes = []

        # tmp = head

        # while tmp:
        #     listnodes.append(tmp)
        #     tmp = tmp.next
        
        # # get the size of the listnodes
        # size = len(listnodes)

        # node_remove_index = size - n
        # if node_remove_index == 0:
        #     return head.next

        # listnodes[node_remove_index - 1].next = listnodes[node_remove_index].next

        # return head

        #space optimized solution
        if not head:
            return None

        
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

        
        