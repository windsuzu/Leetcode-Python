from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = head
        
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next

        return top