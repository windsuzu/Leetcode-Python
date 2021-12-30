from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # the idea is to split the last (k % length) nodes
        # set the new_head and link the last_node to the first_node
        if not head:
            return head

        # 1. find the length and the last_node
        n, last = 1, head
        while last and last.next:
            last = last.next
            n += 1

        if k % n == 0:
            return head

        # 2. Move to the (k % len)th node from the end
        #    by moving [n - (k % len) - 1] times from the beginning
        curr = head
        for _ in range(n - (k % n) - 1):
            curr = curr.next

        # 3. set the newHead, connect last -> first
        newHead, curr.next = curr.next, None
        last.next = head
        return newHead