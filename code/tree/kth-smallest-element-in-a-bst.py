from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # the idea is to use "inorder DFS" with stack
        n = 0
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            n += 1
            if n == k:
                return root.val
            root = root.right