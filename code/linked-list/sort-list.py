from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1. find the mid point
        mid = self.getMid(head)
        mid.next, mid = None, mid.next

        # 2. divide: split the list in half recursively
        left = self.sortList(head)
        right = self.sortList(mid)

        # 3. conquer: merge the lists recursively
        return self.merge(left, right)

    # refer: https://leetcode.com/problems/middle-of-the-linked-list/
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # refer: https://leetcode.com/problems/merge-two-sorted-lists/
    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next
