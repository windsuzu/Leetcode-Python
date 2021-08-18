from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        top = new
        while l1 or l2:
            if l1 is None:
                new.next = l2
                break
            elif l2 is None:
                new.next = l1
                break
                
            if l1.val <= l2.val:
                new.next = l1
                l1 = l1.next
                new = new.next
            elif l1.val > l2.val:
                new.next = l2
                l2 = l2.next
                new = new.next
                
        return top.next