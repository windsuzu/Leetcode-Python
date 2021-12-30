# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        node = root

        # parent (node) exists
        while node:
            # (curr) is a new linked list to store parent (node)'s left and right
            # (dummy) will point to the first node in (curr) as next parent (node)
            curr = dummy = Node(0)

            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next

            # move to next parent/level (node)
            node = dummy.next

            # remove curr/dummy head
            dummy.next = None

        return root