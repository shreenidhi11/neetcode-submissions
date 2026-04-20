# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        slow_next = slow.next
        slow.next = None

        while slow_next:
            tmp = slow_next.next
            slow_next.next = prev
            prev = slow_next
            slow_next = tmp

        temp1 = head
        temp2 = prev

        # initialize the start state of both the lists
        while temp2!=None:
            next1,next2 = temp1.next, temp2.next
            temp1.next = temp2
            temp2.next = next1
            temp1 = next1
            temp2 = next2


            


        # return head







        





        


        