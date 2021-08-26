from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def depth(self, node):
        if not node: return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1
        
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.depth(root)
        return self.ans