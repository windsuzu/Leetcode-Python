# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head is not None and head.next is not None:
            if head.val <= 100_000:
                head.val += 1_000_000
            else:
                return True
            head = head.next
            
        return False