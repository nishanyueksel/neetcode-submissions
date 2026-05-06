# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        llist = None
        while head:
            new_llist = ListNode(head.val)
            new_llist.next = llist
            llist = new_llist
            head = head.next
        return llist
