from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # split the list into odd & even list
        # then connect the last node of odd to the start of even
        if not head:
            return head

        odd, even = head, head.next
        odd_first, even_first = odd, even

        while even and even.next:
            # 1 -------> 3
            #      2
            odd.next = even.next
            odd = odd.next

            # 1 -------> 3
            #      2 --------> 4
            even.next = odd.next
            even = even.next

        odd.next = even_first
        return odd_first