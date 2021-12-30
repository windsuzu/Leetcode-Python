from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # the idea is to have another pointer go "n" steps first
        # and move one pointer at a normal speed
        
        # when the faster pointer reaches the end
        # the normal pointer will be located at the node to be removed
        
        # so in practice, we need to delay 1 step 
        # in order to delete the node by calling "node.next = node.next.next"
        
        dummy, fast = ListNode(0, head), head
        slow = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
