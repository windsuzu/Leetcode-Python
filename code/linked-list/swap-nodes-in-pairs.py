from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # store pointers
            newHead = curr.next
            nextCurr = newHead.next

            # swap
            prev.next = newHead
            newHead.next = curr
            curr.next = nextCurr

            # move to next pair
            prev = curr
            curr = nextCurr

        return dummy.next