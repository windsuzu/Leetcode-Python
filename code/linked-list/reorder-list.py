from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first, find the middle point and seperate the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second, slow.next = slow.next, None
        
        # second, reverse the second linked list
        prev = None
        while second:
            second.next, prev, second = prev, second, second.next
            
        # third, merge two linked lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2
