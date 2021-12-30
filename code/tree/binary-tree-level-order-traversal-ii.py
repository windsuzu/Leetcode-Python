from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, q = deque(), [root] if root else None

        while q:
            res.appendleft([node.val for node in q])
            tmp = []

            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            q = tmp
        return res