from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy
        while current:
            while current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next
        return dummy.next