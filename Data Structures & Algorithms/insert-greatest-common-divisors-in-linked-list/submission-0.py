# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp = head
        while temp.next:
          new_node = ListNode(math.gcd(temp.val, temp.next.val))
          save_current_next = temp.next
          temp.next = new_node
          new_node.next = save_current_next
          temp = save_current_next

        return dummy.next






        