from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_left, curr = dummy, head

        # 1. find the left pointer by moving (left - 1) times
        for _ in range(left - 1):
            prev_left, curr = curr, curr.next

        # 2. reverse (right - left + 1) times
        prev_right = None
        for _ in range(right - left + 1):
            curr.next, curr, prev_right = prev_right, curr.next, curr

        # 3. connect
        prev_left.next.next, prev_left.next = curr, prev_right

        return dummy.next