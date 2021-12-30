from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        
        while queue:
            tmp = []
            for _ in range(len(queue)):
                if node := queue.popleft():
                    tmp.append(node.val)
                    queue.extend([node.left, node.right])
            if tmp:
                res.append(tmp)
        return res