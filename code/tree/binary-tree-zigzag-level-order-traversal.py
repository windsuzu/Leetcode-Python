from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, q = [], [root] if root else None
        i = 0  # even => from start, odd => from end

        while q:
            tmp = []
            res.append([node.val for node in q[:: (-1 if i % 2 == 1 else 1)]])

            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            q = tmp
            i += 1
        return res