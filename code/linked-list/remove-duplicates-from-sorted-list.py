from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use while to check if the value of "current.next" is equal to "val" repeatedly
        dummy = ListNode(0, head)
        cur = dummy.next
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return dummy.next