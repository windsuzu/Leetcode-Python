from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        while True:
            if fast.next is None:
                return slow
            elif fast.next.next is None:
                return slow.next
                        
            fast = fast.next.next
            slow = slow.next