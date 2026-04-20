# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prevGrp = dummy

        def findKthNode(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        while True:
            find_kth_node = findKthNode(prevGrp, k)
            if find_kth_node:
                next_grp = find_kth_node.next
            else:
                break
            
            # start reversing now
            prev, curr = next_grp, prevGrp.next
            while curr != next_grp:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # make the connection changes
            tmp = prevGrp.next
            prevGrp.next = find_kth_node
            prevGrp = tmp

        return dummy.next

        



        