from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the idea of iterative solution is to use two pointers
        
        prev, curr = None, head
        
        # in each iteration, we must do 3 things simultaneously
        # 1. curr.next = prev
        # 2. move "curr" to the next position, which is "curr.next"
        # 3. move "prev" to the next position, which is "curr"
        
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        return prev
    
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tha final layer of the recursive solution is the last node
        
        if not head or not head.next:
            return head
        
        # after the function hit the last node and return itself
        # the previous nodes will do 2 things:
        # 1. set next node points to self
        # 2. point to None
        
        # take "1 -> 2 -> 3 -> null" as an example:
        # after 3 return itself and become new_head
        # 2 will make 3 point to itself and itself point to None
        # None <- 2 <- 3
        # next, 1 will make 2 point to itself and itself point to None
        # None <- 1 <- 2 <- 3   
        
        new_head, head.next.next, head.next = self.reverseListRecursive(head.next), head, None

        return new_head