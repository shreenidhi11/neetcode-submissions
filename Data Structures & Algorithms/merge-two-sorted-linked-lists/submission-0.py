# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head3 = None
        tmp3 = ListNode()

        if not list1 and not list2:
            return None

        while head1!=None and head2!=None:
            if head1.val <= head2.val:
                print("going here")
                newList =  ListNode(head1.val)
                if not head3:
                    print("first node")
                    head3 = newList
                    print(head3.val)
                    tmp3 = head3
                    print(tmp3.val)
                else:
                    print("second nodes")
                    tmp3.next = newList
                    tmp3 = newList
                    print(tmp3.val)
                head1 = head1.next
            else:
                print("going here2")
                newList =  ListNode(head2.val)
                if not head3:
                    head3 = newList
                    tmp3 = head3
                else:
                    tmp3.next = newList
                    tmp3 = newList
                head2 = head2.next
            

        if head1 != None:
            while head1:
                newList =  ListNode(head1.val)
                if not head3:
                    head3 = newList
                    tmp3 = head3
                else:
                    tmp3.next = newList
                    tmp3 = newList
                head1 = head1.next


        if head2 != None:
            while head2:
                newList =  ListNode(head2.val)
                if not head3:
                    head3 = newList
                    tmp3 = head3
                else:
                    tmp3.next = newList
                    tmp3 = newList
                head2 = head2.next


        return head3
        













                


        