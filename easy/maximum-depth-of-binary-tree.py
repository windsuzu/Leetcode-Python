from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        root = [root]
        level = 0

        while root:
            temp = []
            level += 1

            for node in root:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            root = temp
        return level