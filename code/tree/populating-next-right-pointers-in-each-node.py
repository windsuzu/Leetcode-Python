from typing import Optional

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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        # store the root for return
        dummy = root

        # keep looping until we reach the last row
        while root and root.left:
            next_level = root.left

            # here implement the link between nodes of the next level
            while root:
                root.left.next = root.right
                root.right.next = root.next.left if root.next else None
                root = root.next
            root = next_level
        return dummy