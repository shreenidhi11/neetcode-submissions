# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prevGrp = dummy

        while True:
            # get range of the listnodes
            kth = self.group(prevGrp,k)
            if not kth:
                break
            nxtgrp = kth.next

            # start reversing
            prev, curr = kth.next, prevGrp.next

            while curr != nxtgrp:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prevGrp.next
            prevGrp.next = kth
            prevGrp = tmp

        return dummy.next
        
    def group(self,curr,k):
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr

        