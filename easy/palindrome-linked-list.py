from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def genNode(self, node: Optional[ListNode]):
        while node:
            yield node.val
            node = node.next
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        traversed = [node_val for node_val in self.genNode(head)]            
        return traversed == traversed[::-1]