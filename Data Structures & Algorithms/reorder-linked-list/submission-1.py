# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2,4,6,8,10 -> 2,10,4,8,6
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if slow == fast:
            #     break
        
        # break the connection
        # slow is at 6
        tmp = slow.next
        slow.next = None
        prev = None

        # reverse the list now
        curr = tmp
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # prev is pointing to 10->8
        # head is pointing to 2->4->6
        first, second = head, prev
        while second:
            fnext, snext = first.next, second.next
            first.next = second
            second.next = fnext
            first = fnext
            second = snext







        








        