# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# None <- 2 3 -> 4


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        prev = None
        curr = None

        while tmp is not None:
            save = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = save

        return prev

        