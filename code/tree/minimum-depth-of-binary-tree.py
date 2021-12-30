from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        q = deque([root])
        level = 1
        while q:
            for _ in range(len(q)):
                if node := q.popleft():
                    if not node.left and not node.right:
                        return level
                    q.extend([node.left, node.right])
            level += 1
            