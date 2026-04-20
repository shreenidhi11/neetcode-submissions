# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # find the node before the left node
        for _ in range(left - 1):
            prev = prev.next

        # head of the sublist before reversing
        sublist_head = prev.next
        # head becomes the tail after reversing
        sublist_tail = sublist_head

        # find the node till the right node
        for _ in range(right - left):
            sublist_tail = sublist_tail.next

        # get the next node after the right node
        next_node = sublist_tail.next

        # disconnect the list from the right node
        sublist_tail.next = None

        # reverse the sublist now
        reversed_sublist = self.reverseList(sublist_head)

        # connect the previous node to the left with the head of the reversed sublist
        prev.next = reversed_sublist

        # connect the head before reverse to the next node to the right
        sublist_head.next = next_node

        return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev











        

        


        


        