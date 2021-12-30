from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # the idea is to create a dummy node
        # and append the smaller of l1 or l2 to it iteratively
        
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next 
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        
        # append the remaining nodes to it
        tail.next = l1 if l1 else l2
        
        return dummy.next