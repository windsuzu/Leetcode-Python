from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(next=head)
        
        while temp.next and temp.next.val == val:
            temp.next = temp.next.next
        
        head = temp.next
        
        while head:
            while head.next and head.next.val == val:
                head.next = head.next.next
            
            head = head.next
            
        return temp.next